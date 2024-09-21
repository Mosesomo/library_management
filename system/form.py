from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, FloatField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Regexp

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Add Book')

class MemberForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(),
                                                    Regexp('^\\+254[0-9]{9}$',
                                                           message='Invalid phone number.\
                                                               Must start with +254 followed by 9 digits.')],
                        render_kw={"placeholder": "+254xxxxxxxxx"})
    submit = SubmitField('Add Member')
    
    def validate_email(self, email):
        email = Member.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email already exist')

class TransactionForm(FlaskForm):
    book_id = IntegerField('Book ID', validators=[DataRequired(), NumberRange(min=0)])
    member_id = IntegerField('Member ID', validators=[DataRequired(), NumberRange(min=0)])
    issue_date = DateField('Issue Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Issue Book')
