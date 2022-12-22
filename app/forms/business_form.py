from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Business

## Business form
class BusinessForm(FlaskForm):
    name = StringField("name",validators=[DataRequired(),Length(min=1,max=25,message="Business name must be between 1-25 characters.")])
    address = StringField("address", validators=[DataRequired(),Length(min=1,max=50,message="Address must be between 1-50 characters.")])
    city = StringField("city", validators=[DataRequired(),Length(min=1,max=25,message="City must be between 1-25 characters.")])
    state = SelectField("state",choices=['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'])
    zip = StringField("zip",validators=[DataRequired(),Length(min=5,max=5,message="Zip code must be 5 numbers.")])
    price = SelectField("price",choices=['$','$$','$$$','$$$$'])
    phone_number = StringField("phone_number",validators=[DataRequired(), Length(min=10,max=15,message="Please enter a valid phone number.")])
    business_type = StringField("business_type",validators=[DataRequired(),Length(min=1,max=20,message="Business type must be between 1-20 characters.")])
    business_hour = StringField("business_hour",validators=[DataRequired()])
    site = StringField("site")
    submit = SubmitField("submit")
