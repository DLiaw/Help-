from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import BusinessImage

## Business image form
# def valid_image(form,field):
#     business_image = field.data
#     def format = ['jpeg','png', 'jpg','gif']
#     if not format in business_image:
#         raise ValidationError("Images must be in jpeg, png, jpg, or gif format.")
    # if not ".jpeg" in business_image:
    #     raise ValidationError("Images must be in jpeg, png, jpg, or gif format.")
    # if not ".png" in business_image:
    #     raise ValidationError("Images must be in jpeg, png, jpg, or gif format.")
    # if not ".jpg" in review_iamge:
    #     raise ValidationError("Images must be in jpeg, png, jpg, or gif format.")
    # if not ".gif" in business_image:
    #     raise ValidationError("Images must be in jpeg, png, jpg, or gif format.")

class BusinessImageForm(FlaskForm):
    business_image = StringField("business_image",validators=[DataRequired()])
    business_id = StringField("business_id",validators=[DataRequired()])
