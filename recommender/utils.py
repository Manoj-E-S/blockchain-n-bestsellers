__all__ = ['BooksDataset', 'CudaUtils', 'DataLoaderUtils', 'DfUtils', 'EncoderUtils', 'RatingsPredictorGMF', 'RatingsPredictorMLP']

import pandas as pd
from sklearn import model_selection, preprocessing
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import joblib


class CudaUtils:
    @staticmethod
    def get_device():
        if torch.cuda.is_available():
            return torch.device('cuda:0')
        else:
            return torch.device('cpu')


class DataLoaderUtils:
    batch_size = 50
    def __init__(batch_size=50):
        DataLoaderUtils.batch_size = batch_size

    @staticmethod
    def get_train_test(ratings_df):
        train, test = model_selection.train_test_split(
            ratings_df, test_size=0.2, random_state=42, stratify=ratings_df["rating"].values
            )

        train_ds = RatingsDataset(
            users=train["user_id"].values,
            books=train["isbn"].values,
            ratings=train["rating"].values,
            )

        test_ds = RatingsDataset(
            users=test["user_id"].values,
            books=test["isbn"].values,
            ratings=test["rating"].values,
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
    

# Preferably implement on the DB instead of the csv? If csv is dynamically growing that's also fine
class PopularBooksRecommender:
    @staticmethod
    def recommend(rdf_path, n=10):
        ratings_df = DfUtils.get_ratings_df(rdf_path)
        ratings_df = ratings_df.groupby("isbn").filter(lambda x: len(x) > 200)
        sorted_rdf = ratings_df.sort_values("rating", ascending=False)
        rndm_n_of_rated_over_4p5 = sorted_rdf[sorted_rdf["rating"] > 4.5].sample(n)["isbn"].values
        
        return rndm_n_of_rated_over_4p5
    
    @staticmethod
    def recommend_from_genre(rdf_path, genre, n=10):
        ratings_df = DfUtils.get_ratings_df(rdf_path)
        ratings_df = ratings_df[ratings_df["genre"] == genre]
        ratings_df = ratings_df.groupby("isbn").filter(lambda x: len(x) > 200)
        sorted_rdf = ratings_df.sort_values("rating", ascending=False)
        rndm_n_of_rated_over_4p5 = sorted_rdf[sorted_rdf["rating"] > 4.5].sample(n)["isbn"].values
        
        return rndm_n_of_rated_over_4p5
    
    @staticmethod
    def recommend_from_author(rdf_path, author, n=10):
        ratings_df = DfUtils.get_ratings_df(rdf_path)
        ratings_df = ratings_df[ratings_df["author"] == author]
        ratings_df = ratings_df.groupby("isbn").filter(lambda x: len(x) > 200)
        sorted_rdf = ratings_df.sort_values("rating", ascending=False)
        rndm_n_of_rated_over_4p5 = sorted_rdf[sorted_rdf["rating"] > 4.5].sample(n)["isbn"].values
        
        return rndm_n_of_rated_over_4p5

    @staticmethod
    def random_n(rdf_path, n=10):
        ratings_df = DfUtils.get_ratings_df(rdf_path)
        ratings_df = ratings_df.groupby("isbn").filter(lambda x: len(x) > 200)
        rndm_n = ratings_df.sample(n)["isbn"].values
        
        return rndm_n


class RatingsDataset(Dataset):
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


class RatingsPredictorGMF(nn.Module):
    def __init__(self, n_books, n_users, embedding_dim=32, hidden_dim=64):
        super().__init__()
        
        self.user_embed = nn.Embedding(n_users, embedding_dim)
        self.book_embed = nn.Embedding(n_books, embedding_dim)
        self.out = nn.Linear(hidden_dim, 1)


    def forward(self, users, books):
        user_embed = self.user_embed(users)
        book_embed = self.book_embed(books)
        concat = torch.cat([user_embed, book_embed], dim=1) 
        output = torch.sigmoid(self.out(concat)) * 5

        return output


class RatingsPredictorMLP(nn.Module):
    def __init__(self, n_books, n_users, embedding_dim=32, hidden_dim=64):
        super(RatingsPredictorMLP, self).__init__()

        # GMF embeddings
        self.user_embed_gmf = nn.Embedding(n_users, embedding_dim)
        self.book_embed_gmf = nn.Embedding(n_books, embedding_dim)

        # MLP embeddings
        self.user_embed_mlp = nn.Embedding(n_users, embedding_dim)
        self.book_embed_mlp = nn.Embedding(n_books, embedding_dim)
        
        # MLP layers
        self.mlp = nn.Sequential(
            nn.Linear(embedding_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )

        # Output layer
        self.out = nn.Linear(embedding_dim + hidden_dim, 1)


    def forward(self, users, books):
        # GMF part
        user_embed_gmf = self.user_embed_gmf(users)
        book_embed_gmf = self.book_embed_gmf(books)
        gmf = user_embed_gmf * book_embed_gmf # Matrix Dot Product
        
        # MLP part
        user_embed_mlp = self.user_embed_mlp(users)
        book_embed_mlp = self.book_embed_mlp(books)
        mlp_input = torch.cat([user_embed_mlp, book_embed_mlp], dim=1)
        mlp = self.mlp(mlp_input)
        
        # Concatenate GMF and MLP parts
        concat = torch.cat([gmf, mlp], dim=1)

        # Final output
        output = torch.sigmoid(self.out(concat)) * 5

        return output
    

if __name__ == "__main__":
    pop_books = PopularBooksRecommender.recommend("./main_dataset/updated_ratings.csv", n=10)
    print(pop_books)
