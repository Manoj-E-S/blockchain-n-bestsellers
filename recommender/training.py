import numpy as np
from sklearn import model_selection
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Subset

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

from recommender.utils import (
    CudaUtils, DataLoaderUtils, DfUtils, RatingsPredictor
)

class Trainer:
    def __init__(self, opt_lr, sch_gamma, sch_step_size, n_folds, rdf_path):
        self.device = CudaUtils.get_device()

        self.ratings_df = DfUtils.get_ratings_df(rdf_path)
        
        self.mod_n_users = len(self.ratings_df["user_id"].unique())
        self.mod_n_books = len(self.ratings_df["isbn"].unique())
        self.model = RatingsPredictor(self.mod_n_books, self.mod_n_users).to(self.device)

        self.loss_fn = nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=opt_lr)
        self.scheduler = torch.optim.lr_scheduler.StepLR(self.optimizer, sch_step_size, gamma=sch_gamma)
        self.kf = model_selection.KFold(n_splits=n_folds, shuffle=True)


    @staticmethod
    def print_stats(train_fold_losses, val_fold_losses):

        avg_val_losses = np.mean(val_fold_losses, axis=0)
        print("Average Validation Losses:", avg_val_losses)

        avg_train_losses = np.mean(train_fold_losses, axis=0)
        print("Average Validation Losses:", avg_train_losses)

        print("Train Losses (fold: [epochs])")
        for i, x in enumerate(train_fold_losses):
            print(f"{i+1}: {x}")

        print("\nValidation Losses (fold: [epochs])")
        for i, x in enumerate(val_fold_losses):
            print(f"{i+1}: {x}")

        plt.plot(train_fold_losses)
        plt.show()
        plt.plot(val_fold_losses)
        plt.show()

    
    def save_model(self, pth_path):
        torch.save(self.model.state_dict(), pth_path)


    def train_all_batches(self, train_dl):
        train_loss = 0
        self.model.train()
        for batch in train_dl:
            users = batch['users']
            books = batch['books']
            ratings = batch['ratings'].view(-1, 1)

            self.optimizer.zero_grad()
            outputs = self.model(users, books)

            loss = self.loss_fn(outputs, ratings)
            train_loss += loss.item()

            loss.backward()
            self.optimizer.step()
        
        self.scheduler.step()

        return (train_loss / len(train_dl))
    

    def validate_all_batches(self, val_dl):
        val_loss = 0
        self.model.eval()
        with torch.no_grad():
            for batch in val_dl:
                users = batch['users']
                books = batch['books']
                ratings = batch['ratings'].view(-1, 1)

                outputs = self.model(users, books)
                val_loss += self.loss_fn(outputs, ratings).item()

        return (val_loss / len(val_dl))


    def initial_train(self, epochs):
        train_ds = DataLoaderUtils.get_train_test(self.ratings_df)["datasets"][0]
        val_fold_losses = []
        train_fold_losses = []

        for fold, (train_idxs, val_idxs) in enumerate(self.kf.split(train_ds)):
            print(f"Fold {fold + 1}")
            
            train_fold = Subset(train_ds, train_idxs)
            val_fold = Subset(train_ds, val_idxs)

            train_dl = DataLoader(train_fold, batch_size=DataLoaderUtils.batch_size, shuffle=True)
            val_dl = DataLoader(val_fold, batch_size=DataLoaderUtils.batch_size, shuffle=False)

            train_fold_loss = []
            val_fold_loss = []

            for epoch in range(epochs):
                print(f"  Epoch {epoch + 1}")

                # Training
                train_loss_ratio = self.train_all_batches(train_dl)
                train_fold_loss.append(train_loss_ratio)
                print(f"    Train Loss: {train_loss_ratio}")

                # Validation
                val_loss_ratio = self.validate_all_batches(val_dl)
                val_fold_loss.append(val_loss_ratio)
                print(f"    Validation Loss: {val_loss_ratio}")

            train_fold_losses.append(train_fold_loss)
            val_fold_losses.append(val_fold_loss)

        Trainer.print_stats(train_fold_losses, val_fold_losses)
    

    def retrain_model(seld, epochs):
        pass
