from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, User, Review, Business, ReviewImage, BusinessImage
from ..forms import BusinessForm, BusinessImageForm, ReviewForm, ReviewImageForm, SignUpForm, LoginForm
from flask_login import login_required, current_user
from app.api.auth_routes import validation_errors_to_error_messages
from app.api.aws import (upload_file_to_s3, allowed_file, get_unique_filename)
from werkzeug.datastructures import ImmutableMultiDict

business_images_routes = Blueprint("business_iamges", __name__)

## Adding an image for business

# @business_images_routes.route('/new',methods=['POST'])
# @login_required
# def business_image():
#     form = BusinessImageForm()
#     form['csrf_token'].data = request.cookies['csrf_token']
#     if form.validate_on_submit():
#         new_business_image = BusinessImage(
#             business_image = form.data['business_image'],
#             business_id = form.data['business_id']
#         )
#         db.session.add(new_business_image)
#         db.session.commit()
#         res = new_business_image.to_dict()
#         return res
#     return {"errors": form.errors}, 401
@business_images_routes.route('/new',methods=['POST'])
@login_required
def business_image():
    if "image" not in request.files:
        return {"errors": "image required"}, 400

    image = request.files["image"]
    business_id = request.form['business_id']
    if not allowed_file(image.filename):
        return {"errors": "file type not permitted"}, 400

    image.filename = get_unique_filename(image.filename)

    upload = upload_file_to_s3(image)

    if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when we tried to upload
        # so we send back that error message
        return upload, 400

    url = upload["url"]
    # flask_login allows us to get the current user from the request
    new_image = BusinessImage(business_id=business_id, business_image=url)
    db.session.add(new_image)
    db.session.commit()
    return {"url": url}

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

## Delete image for business

@business_images_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_business_image(id):
    image = BusinessImage.query.get(id)
    db.session.delete(image)
    db.session.commit()
    return "successfully deleted"
