from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, User, Review, Business, ReviewImage, BusinessImage
from ..forms import BusinessForm, BusinessImageForm, ReviewForm, ReviewImageForm, SignUpForm, LoginForm
from flask_login import login_required, current_user
from app.api.auth_routes import validation_errors_to_error_messages
review_images_routes = Blueprint("review_iamges", __name__)

## Adding an image for review

@review_images_routes.route('/new',methods=['POST'])
@login_required
def review_image():
    form = ReviewImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_review_image = ReviewImage(
            review_image = form.data['review_image'],
            review_id = form.data['review_id']
        )
        db.session.add(new_review_image)
        db.session.commit()
        return new_review_image.to_dict()
    return {"errors": form.errors}, 401

## Update image for review

@review_images_routes.route('/<int:id>/edit',methods=['PUT'])
@login_required
def update_review_image(id):
    updated_review_image = ReviewImage.query.filter_by(review_id = id).first()
    form = ReviewImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        setattr(updated_review_image, 'review_image', form.data['review_image'])
        db.session.commit()
        res = updated_review_image.to_dict()
        return res
    if form.errors:
        return {"errors": form.errors}, 401
