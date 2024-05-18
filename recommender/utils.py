__all__ = ['BooksDataset', 'CudaUtils', 'DataLoaderUtils', 'DfUtils', 'EncoderUtils', 'RatingsPredictor']

import pandas as pd
from sklearn import model_selection, preprocessing
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import joblib

class BooksDataset(Dataset):
    def __init__(self, users, ratings, books):
        self.users = users
        self.ratings = ratings
        self.books = books

    def __len__(self):
        return len(self.users)

    def __getitem__(self, idx):
        return {
            'users': torch.tensor(self.users[idx], dtype=torch.long),
            'ratings': torch.tensor(self.ratings[idx], dtype=torch.float32),
            'books': torch.tensor(self.books[idx], dtype=torch.long)
        }


class CudaUtils:
    @staticmethod
    def get_device():
        if torch.cuda.is_available():
            return torch.device('cuda:0')
        else:
            return torch.device('cpu')


class DataLoaderUtils:
    def __init__(batch_size=50):
        DataLoaderUtils.batch_size = batch_size

    @staticmethod
    def get_train_test(ratings_df):
        train, test = model_selection.train_test_split(
            ratings_df, test_size=0.2, random_state=42, stratify=ratings_df["rating"].values
            )

        train_ds = BooksDataset(
            users=train["user_id"].values,
            books=train["isbn"].values,
            ratings=train["rating"].values
            )

        test_ds = BooksDataset(
            users=test["user_id"].values,
            books=test["isbn"].values,
            ratings=test["rating"].values
            )
        
        train_dl = DataLoader(train_ds, batch_size=DataLoaderUtils.batch_size, shuffle=True, num_workers=2)
        test_dl = DataLoader(test_ds, batch_size=DataLoaderUtils.batch_size, shuffle=True, num_workers=2)

        return {
            "datasets": (train_ds, test_ds), 
            "dataloders": (train_dl, test_dl)
            }


class DfUtils:
    @staticmethod
    def get_df(df_path):
        return pd.read_csv(df_path)
    
    @staticmethod
    def get_ratings_df(df_path):
        # Get ratings_df from csv, and encoders
        ratings_df = pd.read_csv(df_path)
        userid_encoder, isbn_encoder = EncoderUtils.load_encoders()

        # Preprocess rating_df
        ratings_df["user_id"] = userid_encoder.fit_transform(ratings_df["user_id"].values)
        ratings_df["isbn"] = isbn_encoder.fit_transform(ratings_df["isbn"].values)
        ratings_df = ratings_df[ratings_df["rating"] != 0]

        return ratings_df
    

class EncoderUtils:
    @staticmethod
    def dump_encoders(userid_encoder, isbn_encoder):
        joblib.dump(userid_encoder, './label_encoders/userid_encoder.pkl')
        joblib.dump(isbn_encoder, './label_encoders/isbn_encoder.pkl')
    
    @staticmethod
    def load_encoders():
        try:
            userid_encoder = joblib.load('./label_encoders/userid_encoder.pkl')
            isbn_encoder = joblib.load('./label_encoders/isbn_encoder.pkl')
        except FileNotFoundError:
            userid_encoder = preprocessing.LabelEncoder()
            isbn_encoder = preprocessing.LabelEncoder()
            
        return userid_encoder, isbn_encoder
    

class RatingsPredictor(nn.Module):
    def __init__(self, n_books, n_users):
        super(RatingsPredictor, self).__init__()      
        self.user_embed = nn.Embedding(n_users, 32)
        self.book_embed = nn.Embedding(n_books, 32)
        self.out = nn.Linear(64, 1)


    def forward(self, users, books):
        user_embed = self.user_embed(users)
        book_embed = self.book_embed(books)
        output = torch.cat([user_embed, book_embed], dim=1) 
        output = self.out(output)

        return output
    

