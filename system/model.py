from system import db

# Define the Book model representing books in the library
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    # String representation of the Book model for easier debugging
    def __repr__(self):
        return f'<Book {self.title}>'

# Define the Member model representing library members
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(10), nullable=True)
    debt = db.Column(db.Float, default=0.0)

    # String representation of the Member model for easier debugging
    def __repr__(self):
        return f'<Member {self.name}>'

# Define the Transaction model representing the borrowing and returning of books
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    issue_date = db.Column(db.Date, nullable=False) 
    return_date = db.Column(db.Date, nullable=True)
    fee = db.Column(db.Float, default=0.0)
    
    # Relationship to access the book and member details
    book = db.relationship('Book', backref='transactions')
    member = db.relationship('Member', backref='transactions')

    # String representation of the Transaction model for easier debugging
    def __repr__(self):
        return f'<Transaction {self.id}>'
