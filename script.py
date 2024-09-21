"""This script is for managing our database, all the insertion of data
    and also deletion of data is being done in this script
"""
from system import db, app
from system.model import Member, Transaction, Book


with app.app_context():
    db.create_all()