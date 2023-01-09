from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, User, Review, Business, ReviewImage, BusinessImage
from ..forms import BusinessForm, BusinessImageForm, ReviewForm, ReviewImageForm, SignUpForm, LoginForm
from flask_login import login_required, current_user
from app.api.auth_routes import validation_errors_to_error_messages
business_images_routes = Blueprint("business_iamges", __name__)

## Adding an image for business

@business_images_routes.route('/new',methods=['POST'])
@login_required
def business_image():
    form = BusinessImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_business_image = BusinessImage(
            business_image = form.data['business_image'],
            business_id = form.data['business_id']
        )
        db.session.add(new_business_image)
        db.session.commit()
        res = new_business_image.to_dict()
        return res
    return {"errors": form.errors}, 401

## Update image for business

@business_images_routes.route('/<int:id>/edit',methods=['PUT'])
@login_required
def update_business_image(id):
    updated_business_image = BusinessImage.query.filter_by(business_id = id).first()
    form = BusinessImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        setattr(updated_business_image, 'business_image', form.data['business_image'])
        db.session.commit()
        res = updated_business_image.to_dict()
        return res
    if form.errors:
        return {"errors": form.errors}, 401
