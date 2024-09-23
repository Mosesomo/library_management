"""
    route performing crud operation
"""
from system import app, db
from system.model import Member, Book, Transaction
from flask import render_template, redirect, url_for, request, flash
from system.form import MemberForm, BookForm, TransactionForm, UpdateMemberForm, UpdateBookForm
from datetime import datetime

'''Book CRUD operation'''
# Read books
@app.route('/')
@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)

# create new book
@app.route('/books/add-new-book', methods=['POST', 'GET'])
def newBook():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            stock=form.stock.data
        )
        
        db.session.add(book)
        db.session.commit()
        
        flash('Book added successfully', 'success')
        return redirect(url_for('books'))
    return render_template('add_book.html', form=form)

# update book
@app.route('/books/update-book/<int:book_id>', methods=['POST', 'GET'])
def updateBook(book_id):
    book = Book.query.get_or_404(book_id)
    form = UpdateBookForm()
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.stock = form.stock.data
        db.session.commit()
        flash('Book update successfully', 'primary')
        return redirect(url_for('books', book_id=book.id))
    elif request.method == 'GET':
        form.title.data = book.title
        form.author.data = book.author
        form.stock.data = book.stock
    return render_template('update_book.html', form=form)


# Delete a book
@app.route('/books/delete-book/<int:book_id>', methods=['POST', 'GET'])
def deleteBook(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully', 'danger')
    return redirect(url_for('books'))


'''member CRUD operation'''
# Read member (get)
@app.route('/members')
def members():
    members = Member.query.all()
    return render_template('members.html', members=members)

# create member
@app.route('/members/add-new-member', methods=['POST', 'GET'])
def newMember():
    form = MemberForm()
    if form.validate_on_submit():
        member = Member(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            debt=form.debt.data
        )
        db.session.add(member)
        db.session.commit()
        
        flash('Memeber added successfully', 'success')
        return redirect(url_for('members'))
    return render_template('add_member.html', form=form)


# update member
@app.route('/members/update-member/<int:member_id>', methods=['POST', 'GET'])
def updateMember(member_id):
    member = Member.query.get_or_404(member_id)
    form = UpdateMemberForm()
    if form.validate_on_submit():
        member.email = form.email.data
        member.phone = form.phone.data
        member.debt = form.debt.data
        db.session.commit()
        flash('Member updated succesfully', 'primary')
        return redirect(url_for('members', member_id=member.id))
    elif request.method == 'GET':
        form.email.data = member.email
        form.phone.data = member.phone
        form.debt.data = member.debt
    return render_template('update_member.html', form=form)


# delete member
@app.route('/members/delete-member/<int:member_id>', methods=['POST', 'GET'])
def deleteMember(member_id):
    member = Member.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    flash('Member removed successfully', 'danger')
    return redirect(url_for('members'))
    
'''transaction CRUD operation'''
@app.route('/transactions')
def transactions():
    transactions = Transaction.query.all()
    return render_template('transactions.html', transactions=transactions)


# Search for Books
@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    # Check if the query is not empty
    if query:
        # Search for books where the title or author matches the query
        books = Book.query.filter(
            (Book.title.ilike(f'%{query}%')) | (Book.author.ilike(f'%{query}%'))
        ).all()
    else:
        # If no query is provided, display all books
        books = Book.query.all()
    
    return render_template('books.html', books=books)

# Transaction
@app.route('/transactions/new-transaction', methods=['GET', 'POST'])
def newTransactions():
    form = TransactionForm()

    if form.validate_on_submit():
        # Extract data from the form
        book_id = form.book_id.data
        member_id = form.member_id.data
        issue_date = form.issue_date.data
        return_date = form.return_date.data  # This should now be required on issuance

        # Validate the return date is after the issue date
        if return_date < issue_date:
            flash('Return date cannot be before the issue date.', 'danger')
            return redirect(url_for('newTransactions'))

        # Check if the book exists and has available stock
        book = Book.query.get(book_id)
        if book and book.stock > 0:
            # Calculate the rent fee based on the duration the book is issued for
            days_issued = (return_date - issue_date).days
            rent_fee = days_issued * 50  # Example: KES 50 per day

            # Check if the member's debt will exceed the limit after adding the fee
            member = Member.query.get(member_id)
            if member.debt + rent_fee <= 500:
                # Issue the book and create a new transaction
                new_transaction = Transaction(
                    book_id=book_id, 
                    member_id=member_id, 
                    issue_date=issue_date, 
                    return_date=return_date,
                    fee=rent_fee
                )
                db.session.add(new_transaction)
                
                # Reduce the book stock by 1
                book.stock -= 1
                member.debt += rent_fee  # Add the fee to the member's debt
                db.session.commit()

                flash(f'Book issued successfully! Rent fee: KES {rent_fee}', 'success')
            else:
                flash('Member’s debt exceeds the limit of KES 500.', 'danger')
        else:
            flash('No copies of the book are available.', 'danger')

        return redirect(url_for('transactions'))

    return render_template('add_transaction.html', form=form)
