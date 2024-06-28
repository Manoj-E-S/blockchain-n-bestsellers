import pandas as pd
import ast


class DfUtils:
    @staticmethod
    def get_df(df_path):
        return pd.read_csv(df_path)
    
    @staticmethod
    def get_ratings_df(df_path):
        ratings_df = pd.read_csv(df_path)
        ratings_df = ratings_df[ratings_df["rating"] != 0]

        return ratings_df
    

class PopularBooksRecommender:
    @staticmethod
    def recommend(rdf_path, n=10):
        ratings_df = DfUtils.get_ratings_df(rdf_path)
        ratings_df = ratings_df.groupby("isbn").filter(lambda x: len(x) > 200)
        sorted_rdf = ratings_df.sort_values("rating", ascending=False)
        rndm_n_of_rated_over_4p5 = sorted_rdf[sorted_rdf["rating"] > 4.5].sample(int(n))["isbn"].values
        
        return rndm_n_of_rated_over_4p5
    
    @staticmethod
    def recommend_from_genre(df_path, genre, n=10):
        books_df = DfUtils.get_df(df_path)
        books_df = books_df[books_df['genre'].apply(lambda x: genre in eval(x))]
        rndm_n = books_df.sort_values("avg_rating", ascending=False).sample(int(n))["isbn"].values
        
        return rndm_n
    

    @staticmethod
    def random_n(rdf_path, n=10):
        ratings_df = DfUtils.get_ratings_df(rdf_path)
        ratings_df = ratings_df.groupby("isbn").filter(lambda x: len(x) > 200)
        rndm_n = ratings_df.sample(int(n))["isbn"].values
        
        return rndm_n