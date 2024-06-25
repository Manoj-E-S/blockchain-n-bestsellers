from datetime import datetime

from .db_setup import db

class User(db.Model):
    __tablename__ = "users"

    uId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    login_type = db.Column(db.String(50), nullable=False, default="local")
    contact_no = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(250), nullable=False)

    # Profile stats (including it here for faster queries)
    books_rated = db.Column(db.Integer, nullable=False, default=0)
    date_joined = db.Column(db.Date, nullable=False, default=datetime.now().date())
    exchanges_made = db.Column(db.Integer, nullable=False, default=0)

    # Relationships
    ratings = db.relationship('Rating', backref='user', lazy=True)
    exchanges = db.relationship('Exchange', backref='user', lazy=True)
    trainable_books = db.relationship('TrainableBook', backref='user', lazy=True)
    messages = db.relationship('Message', backref='user', lazy=True)

    def __repr__(self) -> str:
        return f"User Name: {self.name}, Email: {self.email}, uId: {self.uId}"


class Book(db.Model):
    __tablename__ = "books"

    bId = db.Column(db.Integer, primary_key=True)
    ISBN = db.Column(db.String(50), unique=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50))  # nullable=True
    avg_rating = db.Column(db.Float, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    imgUrlSmall = db.Column(db.String(250))  # nullable=True
    imgUrlLarge = db.Column(db.String(250))  # nullable=True
    year_of_publication = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(50), nullable=False)

    # Relationships
    ratings = db.relationship('Rating', backref='book', lazy=True)
    exchanges = db.relationship('Exchange', backref='book', lazy=True)
    trainable_books = db.relationship('TrainableBook', backref='book', lazy=True)

    def __repr__(self) -> str:
        return f"Book Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}"


class Rating(db.Model):
    __tablename__ = "ratings"

    rId = db.Column(db.Integer, primary_key=True)
    uId = db.Column(db.Integer, db.ForeignKey('users.uId'), nullable=False)
    bId = db.Column(db.Integer, db.ForeignKey('books.bId'), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"User Id: {self.uId}, Book Id: {self.bId}, Rating: {self.rating}"
    
class Exchange(db.Model):
    __tablename__ = "exchanges"

    eId = db.Column(db.Integer, primary_key=True)
    uId = db.Column(db.Integer, db.ForeignKey('users.uId'), nullable=False)
    bId = db.Column(db.Integer, db.ForeignKey('books.bId'), nullable=False)

    def __repr__(self) -> str:
        return f"User Id: {self.uId}, Book Id: {self.bId}"


class TrainableBook(db.Model):
    __tablename__ = "trainablebooks"

    tId = db.Column(db.Integer, primary_key=True)
    uId = db.Column(db.Integer, db.ForeignKey('users.uId'), nullable=False)
    bId = db.Column(db.Integer, db.ForeignKey('books.bId'), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"User Id: {self.uId}, Book Id: {self.bId}, Rating: {self.rating}"


class Message(db.Model):
    __tablename__ = "messages"

    mId = db.Column(db.Integer, primary_key=True)
    requestFor = db.Column(db.Integer, db.ForeignKey('books.bId'), nullable=False)
    inReturnFor = db.Column(db.Integer, db.ForeignKey('books.bId'), nullable=False)
    requesterId = db.Column(db.Integer, db.ForeignKey('users.uId'), nullable=False)
    requesteeId = db.Column(db.Integer, db.ForeignKey('users.uId'), nullable=False)
    currentState = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(250), nullable=False)
    eId = db.Column(db.Integer, db.ForeignKey('exchanges.eId'), nullable=False)

    def __repr__(self) -> str:
        return f"Requester Id: {self.requesterId}, Requestee Id: {self.requesteeId}, Message: {self.message}"

# Creating a table to reduce CPU usage, and directly query the stats (will reduce query time)
class ServerStats(db.Model):
    __tablename__ = "server_stats"

    sId = db.Column(db.Integer, primary_key=True)
    books_exchanged = db.Column(db.Integer, nullable=False)
    number_of_users = db.Column(db.Integer, nullable=False)
    books_available = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Books Exchanged: {self.books_exchanged}, Number of Users: {self.number_of_users}, Books Available: {self.books_available}"