from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import BusinessImage

## Business image form
def valid_image(form,field):
    review_image = field.data
    if not ".jpeg" or ".png" or ".jpg" or ".gif" in business_image:
        raise ValidationError("Images must be in jpeg, png, jpg, or gif format.")

class BusinessImageForm(FlaskForm):
    business_image = StringField("business_image",validators=[DataRequired(),valid_image])
