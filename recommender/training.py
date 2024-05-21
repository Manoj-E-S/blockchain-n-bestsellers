import numpy as np
from sklearn import model_selection
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Subset

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

from utils import (
    CudaUtils, DataLoaderUtils, DfUtils, EncoderUtils, RatingsPredictorGMF, RatingsPredictorMLP
)

class Trainer:
    def __init__(self, opt_lr, sch_gamma, sch_step_size, n_folds, device, n_batches=None):
        userid_encoder, isbn_encoder = EncoderUtils.load_encoders()
        
        self.mod_n_books = len(isbn_encoder.classes_)
        self.mod_n_users = len(userid_encoder.classes_)
        self.batch_size = DataLoaderUtils.batch_size if not n_batches else n_batches
        
        self.model = RatingsPredictorGMF(
                n_books=self.mod_n_books,
                n_users=self.mod_n_users
            ).to(device)
        
        self.loss_fn = nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=opt_lr)
        self.scheduler = torch.optim.lr_scheduler.StepLR(self.optimizer, sch_step_size, gamma=sch_gamma)
        self.kf = model_selection.KFold(n_splits=n_folds, shuffle=True)


    def print_train_stats(self, train_fold_losses, val_fold_losses):

        print()
        avg_val_losses = np.mean(val_fold_losses, axis=0)
        print("Average Validation Losses:", avg_val_losses)

        avg_train_losses = np.mean(train_fold_losses, axis=0)
        print("Average Validation Losses:", avg_train_losses)

        print()
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


    def print_test_stats(self, error_counts, error_ratios):
        print()
        print(f"Total Number of batches: {len(error_ratios)}")
        print(f"Minimum Errors per batch: {min(error_counts)}")
        print(f"Maximum Errors per batch: {max(error_counts)}")
        print(f"Average Errors ratio: {sum(error_counts)/(self.batch_size*len(error_counts))}")
        print()

        plt.plot(error_ratios)
        plt.xlabel("Batch No.")
        plt.ylabel("Error Ratio")
        plt.show()

        plt.hist(error_ratios, bins=50)
        plt.xlabel("Error Ratio")
        plt.ylabel("Occurance Frequency")
        plt.show()

    
    def save_model(self, pth_path):
        torch.save(self.model.state_dict(), pth_path)


    def train_all_batches(self, train_dl, device):
        train_loss = 0
        self.model.train()
        for batch in train_dl:
            users = batch['users'].to(device)
            books = batch['books'].to(device)
            ratings = batch['ratings'].view(-1, 1).to(device)

            self.optimizer.zero_grad()
            outputs = self.model(users, books)

            loss = self.loss_fn(outputs, ratings)
            train_loss += loss.item()

            loss.backward()
            self.optimizer.step()
        
        self.scheduler.step()

        return (train_loss / len(train_dl))
    

    def validate_all_batches(self, val_dl, device):
        val_loss = 0
        self.model.eval()
        with torch.no_grad():
            for batch in val_dl:
                users = batch['users'].to(device)
                books = batch['books'].to(device)
                ratings = batch['ratings'].view(-1, 1).to(device)

                outputs = self.model(users, books)
                val_loss += self.loss_fn(outputs, ratings).item()

        return (val_loss / len(val_dl))


    def initial_train(self, epochs, train_ds, device):
        val_fold_losses = []
        train_fold_losses = []

        for fold, (train_idxs, val_idxs) in enumerate(self.kf.split(train_ds)):
            print(f"Fold {fold + 1}")
            
            train_fold = Subset(train_ds, train_idxs)
            val_fold = Subset(train_ds, val_idxs)

            train_dl = DataLoader(train_fold, batch_size=self.batch_size, shuffle=True)
            val_dl = DataLoader(val_fold, batch_size=self.batch_size, shuffle=False)

            train_fold_loss = []
            val_fold_loss = []

            for epoch in range(epochs):
                print(f"  Epoch {epoch + 1}")

                # Training
                train_loss_ratio = self.train_all_batches(train_dl, device)
                train_fold_loss.append(train_loss_ratio)
                print(f"    Train Loss: {train_loss_ratio}")

                # Validation
                val_loss_ratio = self.validate_all_batches(val_dl, device)
                val_fold_loss.append(val_loss_ratio)
                print(f"    Validation Loss: {val_loss_ratio}")

            train_fold_losses.append(train_fold_loss)
            val_fold_losses.append(val_fold_loss)

        # Use the return values to print stats if needed
        return (train_fold_losses, val_fold_losses)
    
    
    def test_all_batches(self, test_dl, device, debug_flag=False):
        error_counts = []
        error_ratios = []
        error_count = 0

        self.model.eval()
        with torch.no_grad():
            for i, batch in enumerate(test_dl):
                users = batch['users'].to(device)
                books = batch['books'].to(device)
                ratings = batch['ratings'].view(-1, 1).to(device)

                output = self.model(users, books)

                for j, (o, r) in enumerate(zip(output, ratings)):
                    if abs(o - r) > 0.7:
                        print(f"{i, j} : {abs(o - r).item()}") if debug_flag else None
                        error_count += 1

                print() if debug_flag else None

                error_counts.append(error_count)

                erred_ratio = error_count/len(users)
                error_ratios.append(erred_ratio)

                error_count = 0
        
        return (error_counts, error_ratios)
    

    def retrain_model(self, epochs):
        raise NotImplementedError


if __name__ == "__main__":
    device = CudaUtils.get_device()
    model_trainer = Trainer(
            opt_lr=0.001,
            sch_gamma=0.9,
            sch_step_size=1,
            device=device,
            n_folds=3
        )
    
    
    ratings_df = DfUtils.get_ratings_df("./main_dataset/updated_ratings.csv")
    split_ds_dl = DataLoaderUtils.get_train_test(ratings_df)
    train_ds = split_ds_dl["datasets"][0]
    test_dl = split_ds_dl["dataloders"][1]

    # Training and Validation (on train_ds)
    train_fold_losses, val_fold_losses = model_trainer.initial_train(epochs=2, train_ds=train_ds, device=device)
    model_trainer.print_train_stats(train_fold_losses, val_fold_losses)

    # Testing (on test_dl)
    error_counts, error_ratios = model_trainer.test_all_batches(test_dl, device)
    model_trainer.print_test_stats(error_counts, error_ratios)

    model_trainer.save_model("./models/matfac_model.pth")