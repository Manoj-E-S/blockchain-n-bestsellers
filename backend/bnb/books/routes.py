from flask import Blueprint, request
from ..middleware.authMiddleware import auth_middleware #TODO: Add middleware to all routes

from ..recommender.utils import (
    PopularBooksRecommender,
    DfUtils,
)

BOOK_DATASET_PATH = "../../../recommender/main_dataset/updated_books.csv"
BOOKS_DF = DfUtils.get_books_df(BOOK_DATASET_PATH)

############ DEV ONLY
from ..schema import Book
import csv
############ DEV ONLY

from ..db_setup import get_db

_db = get_db()

book_bp = Blueprint("books", __name__, url_prefix="/books")

@book_bp.route("/getGenres")
def getGenres():
    genres = {'biography': 16816, 'history': 16813, 'crime': 13876, 'adventure': 6, 'thriller': 13876, 'mystery': 13877, 'humor': 5, 'fiction': 622, 'paranormal': 8934, 'fantasy': 8936, 'romance': 12362, 'young': 1593, 'adult': 1593, 'children': 3946, 'poetry': 281, 'graphic': 596, 'comic': 596, 'horror': 1, 'nonfiction': 9, 'science': 7, 'detective': 4, 'psychology': 2, 'historical': 2}
    return genres, 200


# TODO: need to change title length to 250
@book_bp.route("/addBooksToDb")
def addBooksToDb():
    with open('C:/Users/antri/OneDrive/Desktop/Coding/bnb/backend/bnb/books/updated_books.csv', 'r') as file:
        booksCsv = csv.reader(file)
        for i, row in enumerate(booksCsv):
            try:
                if i == 100:
                    break
                if i == 0:
                    continue
                else:
                    book = Book(
                        ISBN=row[0],
                        title=row[1],
                        genre=row[8],
                        avg_rating=float(row[11]),
                        author=row[2],
                        imgUrlSmall=row[5],
                        imgUrlLarge=row[6],
                        year_of_publication=row[3],
                        publisher=row[4]
                    )
                    _db.session.add(book)
            except Exception as e:
                print(e)
        _db.session.commit()
    return "100 Books added to DB", 200


@book_bp.route("/nPopularBooks/<n>", methods=["GET"])
def getNPopularBooks(n=10):
    pop_isbns = PopularBooksRecommender.recommend(BOOK_DATASET_PATH, n)
    pop_books_df = BOOKS_DF[BOOKS_DF["isbn"].isin(pop_isbns)]
    pop_books = [
        {
            "isbn": isbn,
            "title": title,
            "genres": genres,
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
            list(eval(pop_books_df["genre"])),
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
            "genres": genres,
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
            list(eval(pop_books_df["genre"])),
            pop_books_df["s_img_url"],
            pop_books_df["l_img_url"],
            pop_books_df["pub_year"],
            pop_books_df["publisher"]
        )
    ]

    return pop_books, 200


@book_bp.route("/nRandomBooks/<n>", methods=["GET"])
def getNRandomBooks(n=10):
    random_isbns = PopularBooksRecommender.random_n(BOOK_DATASET_PATH, n)
    random_books_df = BOOKS_DF[BOOKS_DF["isbn"].isin(random_isbns)]
    random_books = [
        {
            "isbn": isbn,
            "title": title,
            "genres": genres,
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
            list(eval(random_books_df["genre"])),
            random_books_df["s_img_url"],
            random_books_df["l_img_url"],
            random_books_df["pub_year"],
            random_books_df["publisher"]
        )
    ]

    return random_books, 200