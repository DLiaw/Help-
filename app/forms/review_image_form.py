from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import ReviewImage

## Review image form
# def valid_image(form,field):
#     review_image = field.data
#     if not ".jpeg" in review_image:
#         raise ValidationError("Images must be in jpeg, png, jpg, or gif format.")
#     if not ".png" in review_image:
#         raise ValidationError("Images must be in jpeg, png, jpg, or gif format.")
#     if not ".jpg" in review_iamge:
#         raise ValidationError("Images must be in jpeg, png, jpg, or gif format.")
#     if not ".gif" in review_image:
#         raise ValidationError("Images must be in jpeg, png, jpg, or gif format.")

class ReviewImageForm(FlaskForm):
    review_image = StringField("review_image",validators=[DataRequired()])
    review_id = StringField('review_id', validators=[DataRequired()])
