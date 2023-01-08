from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def check_email(form, field):
    email = form.data['email']
    if not "@" in email or not '.' in email:
        raise ValidationError('Please enter a valid email.')



class SignUpForm(FlaskForm):
    # username = StringField('username', validators=[DataRequired(), username_exists])
    first_name = StringField('first_name',validators=[DataRequired(),Length(min=1,max=25,message="First name cannot be greater than 25 characters")])
    last_name = StringField('last_name',validators=[DataRequired(),Length(min=1,max=25,message="Last name cannot be greater than 25 characters")])
    email = StringField('email', validators=[DataRequired(), check_email])
    password = StringField('password', validators=[DataRequired()])
