"""This script is for managing our database, all the insertion of data
    and also deletion of data is being done in this script
"""
from system import db, app
from system.model import Member, Transaction, Book


with app.app_context():
    db.create_all()
    
    book1 = Book(
        title="To Kill a Mockingbird",
        author="Harper Lee",
        stock=12
    )
    db.session.add(book1)
    
    book2 = Book(
        title="1984",
        author="George Orwell",
        stock=15
    )
    db.session.add(book2)
    
    book3 = Book(
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        stock=10
    )
    db.session.add(book3)
    
    book4 = Book(
        title="The Catcher in the Rye",
        author="J.D. Salinger",
        stock=8
    )
    db.session.add(book4)
    
    book5 = Book(
        title="Pride and Prejudice",
        author="Jane Austen",
        stock=12
    )
    db.session.add(book5)
    
    member1 = Member(
        name="Moses Omondi",
        email="moses@gmail.com",
        phone="+25474353426"
    )
    
    db.session.add(member1)
    
    member2 = Member(
        name="Esther Njoki",
        email="esther@gmail.com",
        phone="+25474353426"
    )
    
    db.session.add(member2)
    
    member3 = Member(
        name="Juma Atlas",
        email="juma@gmail.com",
        phone="+25474353426"
    )
    
    db.session.add(member3)
    
    member4 = Member(
        name="David Moya",
        email="david@gmail.com",
        phone="+25474353426"
    )
    
    db.session.add(member4)
    
    db.session.commit()
    
    books = Book.query.all()
    for book in books:
        print(book)
        
    members = Member.query.all()
    for member in members:
        print(member)