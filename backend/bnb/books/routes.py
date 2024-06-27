from flask import Blueprint, request
from ..middleware.authMiddleware import auth_middleware #TODO: Add middleware to all routes

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

@book_bp.route("/getBooks")
def getBooks():
    with open('C:/Users/antri/OneDrive/Desktop/Coding/bnb/backend/bnb/books/updated_books.csv', 'r') as file:
        booksCsv = csv.reader(file)
        arr = []
        # append only first 100 lines then break
        for i, row in enumerate(booksCsv):
            if i == 0:
                keys = row
            elif i < 100:
                arr.append({keys[j]: row[j] for j in range(len(row))})
            if i == 100:
                break
    return arr, 200

# TODO: need to change title length to 250
# @book_bp.route("/addBooksToDb")
# def addBooksToDb():
#     with open('C:/Users/antri/OneDrive/Desktop/Coding/bnb/backend/bnb/books/updated_books.csv', 'r') as file:
#         booksCsv = csv.reader(file)
#         for i, row in enumerate(booksCsv):
#             try:
#                 if i == 100:
#                     break
#                 if i == 0:
#                     continue
#                 else:
#                     book = Book(
#                         ISBN=row[0],
#                         title=row[1],
#                         genre=row[8],
#                         avg_rating=float(row[11]),
#                         author=row[2],
#                         imgUrlSmall=row[5],
#                         imgUrlLarge=row[6],
#                         year_of_publication=row[3],
#                         publisher=row[4]
#                     )
#                     _db.session.add(book)
#             except Exception as e:
#                 print(e)
#         _db.session.commit()
#     return "100 Books added to DB", 200

