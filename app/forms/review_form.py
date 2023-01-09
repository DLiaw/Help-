from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Review


## Review form
class ReviewForm(FlaskForm):
    review = TextAreaField("review",validators=[DataRequired(''),Length(min=5,max=2500,message="Your review must be between 5 and 2500 characters.")])
    stars = IntegerField("stars",validators=[DataRequired('Please choose between 1 and 5 stars.')])
