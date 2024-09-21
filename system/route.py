'''
    route performing crud operation
'''
from system import app
from flask import render_template, redirect, url_for, request, flash
from system.form import MemberForm, BookForm, TransactionForm

# Book CRUD operation
@app.route('/')
@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/books/add-new-book', methods=['POST', 'GET'])
def newBook():
    form = BookForm()
    if form.validate_on_submit():
        pass
    return render_template('add_book.html', form=form)

# member CRUD operation
@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/members/add-new-member', methods=['POST', 'GET'])
def newMember():
    form = MemberForm()
    if form.validate_on_submit():
        pass
    return render_template('add_member.html', form=form)
    

# transaction CRUD operation
@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/transactions/add-transaction', methods=['POST', 'GET'])
def newTransaction():
    form = TransactionForm()
    if form.validate_on_submit():
        pass
    return render_template('add_transaction.html', form=form)

