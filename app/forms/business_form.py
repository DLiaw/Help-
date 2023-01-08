from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Business

def valid_site(form,field):
    site = field.data
    if not ".com"  in site:
        raise ValidationError("Please enter a valid site address.")
## Business form
class BusinessForm(FlaskForm):
    owner_id = StringField('owner_id', validators=[DataRequired()])
    name = StringField("name",validators=[DataRequired('Please enter business name.'),Length(min=1,max=25,message="Business name must be between 1-25 characters.")])
    address = StringField("address", validators=[DataRequired('Please provide an address.'),Length(min=1,max=50,message="Address must be between 1-50 characters.")])
    city = StringField("city", validators=[DataRequired('Please enter a city.'),Length(min=1,max=25,message="City must be between 1-25 characters.")])
    state = SelectField("state",choices=['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'],validators=[DataRequired('Please select a state.')])
    zip = StringField("zip",validators=[DataRequired('Please enter a zip code.'),Length(min=5,max=5,message="Zip code must be 5 numbers.")])
    price = SelectField("price",choices=['$','$$','$$$','$$$$'], validators=[DataRequired('Please select a price.')])
    phone_number = StringField("phone_number",validators=[DataRequired('Please enter a phone number.'), Length(min=10,max=15,message="Please enter a valid phone number.")])
    business_type = StringField("business_type",validators=[DataRequired('Please enter a business type.'),Length(min=1,max=20,message="Business type must be between 1-20 characters.")])
    monOpen = StringField('monOpen',validators=[DataRequired()])
    tueOpen = StringField('tueOpen',validators=[DataRequired()])
    wedOpen = StringField('wedOpen',validators=[DataRequired()])
    thuOpen = StringField('thuOpen',validators=[DataRequired()])
    friOpen = StringField('friOpen',validators=[DataRequired()])
    satOpen = StringField('satOpen',validators=[DataRequired()])
    sunOpen = StringField('sunOpen',validators=[DataRequired()])
    monClose = StringField('monClose',validators=[DataRequired()])
    tueClose = StringField('tueClose',validators=[DataRequired()])
    wedClose = StringField('wedClose',validators=[DataRequired()])
    thuClose = StringField('thuClose',validators=[DataRequired()])
    friClose = StringField('friClose',validators=[DataRequired()])
    satClose = StringField('satClose',validators=[DataRequired()])
    sunClose = StringField('sunClose',validators=[DataRequired()])
    site = StringField("site",validators=[DataRequired('Please enter site address here.'), valid_site])

## fix all back end for business form including model
