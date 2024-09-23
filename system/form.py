from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, FloatField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Regexp, ValidationError
from system.model import Member

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Add Book')
    
class UpdateBookForm(FlaskForm):
    title = StringField('Title')
    author = StringField('Author')
    stock = IntegerField('Stock', validators=[NumberRange(min=0)])
    submit = SubmitField('Update Book')

class MemberForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(),
                                                    Regexp('^\\+254[0-9]{9}$',
                                                           message='Invalid phone number.\
                                                               Must start with +254 followed by 9 digits.')],
                        render_kw={"placeholder": "+254xxxxxxxxx"})
    debt = FloatField('Debt balance', validators=[DataRequired()])
    submit = SubmitField('Add Member')
    
    def validate_email(self, email):
        email = Member.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email already exist')

class UpdateMemberForm(FlaskForm):
    email = StringField('Email')
    phone = StringField('Phone Number', validators=[Regexp('^\\+254[0-9]{9}$',
                                                           message='Invalid phone number.\
                                                               Must start with +254 followed by 9 digits.')]
                        )
    debt = FloatField('Debt balance', validators=[DataRequired()])
    submit = SubmitField('Update Member')

class TransactionForm(FlaskForm):
    book_id = IntegerField('Book ID', validators=[DataRequired(), NumberRange(min=0)])
    member_id = IntegerField('Member ID', validators=[DataRequired(), NumberRange(min=0)])
    issue_date = DateField('Issue Date', format='%Y-%m-%d', validators=[DataRequired()])
    return_date = DateField('Return Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Issue Book')
