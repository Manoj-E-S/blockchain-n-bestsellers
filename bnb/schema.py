from datetime import datetime
from . import get_db

_db = get_db()

# Adding an Association table, to manage m:n relationship between users and messages (may change back to 1:n table)
user_messages = _db.Table('user_messages',
    _db.Column('uId', _db.Integer, _db.ForeignKey('users.uId'), primary_key=True),
    _db.Column('mId', _db.Integer, _db.ForeignKey('messages.mId'), primary_key=True)
)

class User(_db.Model):
    __tablename__ = "users"

    uId = _db.Column(_db.Integer, primary_key=True)
    name = _db.Column(_db.String(50), nullable=False)
    email = _db.Column(_db.String(50), unique=True, nullable=False)
    password = _db.Column(_db.String(50), nullable=False)
    location = _db.Column(_db.String(50), nullable=False)
    login_type = _db.Column(_db.String(50), nullable=False)
    contact_no = _db.Column(_db.String(50), nullable=False)

    # Profile stats (including it here for faster queries)
    books_rated = _db.Column(_db.Integer, nullable=False, default=0)
    date_joined = _db.Column(_db.Date, nullable=False, default=datetime.now().date())
    exchanges_made = _db.Column(_db.Integer, nullable=False, default=0)

    # Relationships
    ratings = _db.relationship('Rating', backref='user', lazy=True)
    exchanges = _db.relationship('Exchange', backref='user', lazy=True)
    trainable_books = _db.relationship('TrainableBook', backref='user', lazy=True)
    messages = _db.relationship('Message', secondary=user_messages, backref=_db.backref('users', lazy=True))

    def __repr__(self) -> str:
        return f"User Name: {self.name}, Email: {self.email}, uId: {self.uId}"


class Book(_db.Model):
    __tablename__ = "books"

    bId = _db.Column(_db.Integer, primary_key=True)
    ISBN = _db.Column(_db.String(50), unique=True, nullable=False)
    title = _db.Column(_db.String(50), nullable=False)
    genre = _db.Column(_db.String(50))  # nullable=True
    avg_rating = _db.Column(_db.Float, nullable=False)
    author = _db.Column(_db.String(50), nullable=False)
    imgUrlSmall = _db.Column(_db.String(250))  # nullable=True
    imgUrlLarge = _db.Column(_db.String(250))  # nullable=True
    year_of_publication = _db.Column(_db.String(50), nullable=False)
    publisher = _db.Column(_db.String(50), nullable=False)

    # Relationships
    ratings = _db.relationship('Rating', backref='book', lazy=True)
    exchanges = _db.relationship('Exchange', backref='book', lazy=True)
    trainable_books = _db.relationship('TrainableBook', backref='book', lazy=True)

    def __repr__(self) -> str:
        return f"Book Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}"


class Rating(_db.Model):
    __tablename__ = "ratings"

    rId = _db.Column(_db.Integer, primary_key=True)
    uId = _db.Column(_db.Integer, _db.ForeignKey('users.uId'), nullable=False)
    bId = _db.Column(_db.Integer, _db.ForeignKey('books.bId'), nullable=False)
    rating = _db.Column(_db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"User Id: {self.uId}, Book Id: {self.bId}, Rating: {self.rating}"
    
class Exchange(_db.Model):
    __tablename__ = "exchanges"

    eId = _db.Column(_db.Integer, primary_key=True)
    uId = _db.Column(_db.Integer, _db.ForeignKey('users.uId'), nullable=False)
    bId = _db.Column(_db.Integer, _db.ForeignKey('books.bId'), nullable=False)

    def __repr__(self) -> str:
        return f"User Id: {self.uId}, Book Id: {self.bId}"


class TrainableBook(_db.Model):
    __tablename__ = "trainablebooks"

    tId = _db.Column(_db.Integer, primary_key=True)
    uId = _db.Column(_db.Integer, _db.ForeignKey('users.uId'), nullable=False)
    bId = _db.Column(_db.Integer, _db.ForeignKey('books.bId'), nullable=False)
    rating = _db.Column(_db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"User Id: {self.uId}, Book Id: {self.bId}, Rating: {self.rating}"


class Message(_db.Model):
    __tablename__ = "messages"

    mId = _db.Column(_db.Integer, primary_key=True)
    requestFor = _db.Column(_db.Integer, _db.ForeignKey('books.bId'), nullable=False)
    inReturnFor = _db.Column(_db.Integer, _db.ForeignKey('books.bId'), nullable=False)
    requesterId = _db.Column(_db.Integer, _db.ForeignKey('users.uId'), nullable=False)
    requesteeId = _db.Column(_db.Integer, _db.ForeignKey('users.uId'), nullable=False)
    currentState = _db.Column(_db.String(50), nullable=False)
    message = _db.Column(_db.String(250), nullable=False)
    eId = _db.Column(_db.Integer, _db.ForeignKey('exchanges.eId'), nullable=False)

    def __repr__(self) -> str:
        return f"Requester Id: {self.requesterId}, Requestee Id: {self.requesteeId}, Message: {self.message}"

    # Random message data
    # message = Message(requestFor=1, inReturnFor=1, requesterId=1, requesteeId=1, currentState="Pending", message="Hey, I am interested in exchanging my book with yours!")

# Creating a table to reduce CPU usage, and directly query the stats (will reduce query time)
class ServerStats(_db.Model):
    __tablename__ = "server_stats"

    sId = _db.Column(_db.Integer, primary_key=True)
    books_exchanged = _db.Column(_db.Integer, nullable=False)
    number_of_users = _db.Column(_db.Integer, nullable=False)
    books_available = _db.Column(_db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Books Exchanged: {self.books_exchanged}, Number of Users: {self.number_of_users}, Books Available: {self.books_available}"