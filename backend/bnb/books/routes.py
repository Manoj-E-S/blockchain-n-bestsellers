import os

from flask import Blueprint, request
from ..middleware.authMiddleware import auth_middleware #TODO: Add middleware to all routes

from ..recommender.utils import (
    PopularBooksRecommender,
    DfUtils,
)

############ DEV ONLY
from ..schema import Book
import csv
############ DEV ONLY

from ..db_setup import get_db

_db = get_db()

book_bp = Blueprint("books", __name__, url_prefix="/books")


BOOK_DATASET_PATH = os.path.join(os.path.dirname(__file__), "../data_store/updated_books.csv")
RATING_DATASET_PATH = os.path.join(os.path.dirname(__file__), "../data_store/updated_ratings.csv")
BOOKS_DF = DfUtils.get_df(BOOK_DATASET_PATH)


@book_bp.route("/getGenres")
def getGenres():
    genres = {'biography': 16816, 'history': 16813, 'crime': 13876, 'adventure': 6, 'thriller': 13876, 'mystery': 13877, 'humor': 5, 'fiction': 622, 'paranormal': 8934, 'fantasy': 8936, 'romance': 12362, 'young': 1593, 'adult': 1593, 'children': 3946, 'poetry': 281, 'graphic': 596, 'comic': 596, 'horror': 1, 'nonfiction': 9, 'science': 7, 'detective': 4, 'psychology': 2, 'historical': 2}
    return genres, 200


@book_bp.route("/nPopularBooks/<n>", methods=["GET"])
def getNPopularBooks(n=10):
    pop_isbns = PopularBooksRecommender.recommend(RATING_DATASET_PATH, n)
    pop_books_df = BOOKS_DF[BOOKS_DF["isbn"].isin(pop_isbns)]
    pop_books = [
        {
            "isbn": isbn,
            "title": title,
            "genres": list(eval(genres)),
            "avg_rating": avg_rating,
            "author": author,
            "imgUrlSmall": imgUrlSmall,
            "imgUrlLarge": imgUrlLarge,
            "year_of_publication": year_of_publication,
            "publisher": publisher
        }
        for isbn, title, author, avg_rating, genres, imgUrlSmall, imgUrlLarge, year_of_publication, publisher in zip(
            pop_books_df["isbn"],
            pop_books_df["title"],
            pop_books_df["author"],
            pop_books_df["avg_rating"],
            pop_books_df["genre"],
            pop_books_df["s_img_url"],
            pop_books_df["l_img_url"],
            pop_books_df["pub_year"],
            pop_books_df["publisher"]
        )
    ]

    return pop_books, 200


@book_bp.route("/nPopularGenreBooks/<genre>/<n>", methods=["GET"])
def getNPopularGenreBooks(genre, n=10):
    pop_isbns = PopularBooksRecommender.recommend_from_genre(BOOK_DATASET_PATH, genre, n)
    pop_books_df = BOOKS_DF[BOOKS_DF["isbn"].isin(pop_isbns)]
    pop_books = [
        {
            "isbn": isbn,
            "title": title,
            "genres": list(eval(genres)),
            "avg_rating": avg_rating,
            "author": author,
            "imgUrlSmall": imgUrlSmall,
            "imgUrlLarge": imgUrlLarge,
            "year_of_publication": year_of_publication,
            "publisher": publisher
        }
        for isbn, title, author, avg_rating, genres, imgUrlSmall, imgUrlLarge, year_of_publication, publisher in zip(
            pop_books_df["isbn"],
            pop_books_df["title"],
            pop_books_df["author"],
            pop_books_df["avg_rating"],
            pop_books_df["genre"],
            pop_books_df["s_img_url"],
            pop_books_df["l_img_url"],
            pop_books_df["pub_year"],
            pop_books_df["publisher"]
        )
    ]

    return pop_books, 200


@book_bp.route("/nRandomBooks/<n>", methods=["GET"])
def getNRandomBooks(n=10):
    random_isbns = PopularBooksRecommender.random_n(RATING_DATASET_PATH, n)
    random_books_df = BOOKS_DF[BOOKS_DF["isbn"].isin(random_isbns)]
    random_books = [
        {
            "isbn": isbn,
            "title": title,
            "genres": list(eval(genres)),
            "avg_rating": avg_rating,
            "author": author,
            "imgUrlSmall": imgUrlSmall,
            "imgUrlLarge": imgUrlLarge,
            "year_of_publication": year_of_publication,
            "publisher": publisher
        }
        for isbn, title, author, avg_rating, genres, imgUrlSmall, imgUrlLarge, year_of_publication, publisher in zip(
            random_books_df["isbn"],
            random_books_df["title"],
            random_books_df["author"],
            random_books_df["avg_rating"],
            random_books_df["genre"],
            random_books_df["s_img_url"],
            random_books_df["l_img_url"],
            random_books_df["pub_year"],
            random_books_df["publisher"]
        )
    ]

    return random_books, 200