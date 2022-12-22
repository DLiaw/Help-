from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, User, Review, Business, ReviewImage, BusinessImage
from ..forms import BusinessForm, BusinessImageForm, ReviewForm, ReviewImageForm, SignUpForm, LoginForm
from flask_login import login_required, current_user
review_routes = Blueprint("reviews", __name__)

## Get all reviews
@review_routes.route('', methods=['GET'])
def all_reviews():
    reviews = Review.query.all()
    result = []
    return {'reviews': [review.to_dict() for review in reviews]}
    # for review in reviews:
    #     # key into join tables to_dict() if its one to many for in it
    #     images = review.review_images
    #     images_list = [image.to_dict() for image in images]
    #     reviewer = review.users.to_dict()
    #     review_data = review.to_dict()
    #     review_data['images'] = images_list
    #     review_data['user'] = reviewer
    #     result.append(review_data)
    # return jsonify({'reviews': result})


## Reviews by current user
@review_routes.route('/my-reviews',methods=['GET'])
@login_required
def user_reviews():
    user = current_user.id
    reviews = Review.query.filter_by(user_id = user).first()
    user_reviews = [review.to_dict() for review in reviews]
    return user_reviews


## Update a review
@review_routes.route('/<int:review_id>', methods=["PUT"])
@login_required
def update_review(review_id):
    review = Review.query.filter_by(id = review_id).first()
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        setattr(review,'review', form.data['review'])
        setattr(review,'stars', form.data['stars'])
    if form.errors:
        return "Invalid Data"

    db.session.commit()
    res = review.to_dict()
    return res

## Delete a review
@review_routes.route('/<int:review_id>', methods=['DELETE'])
@login_required
def delete_review(review_id):
    review = Review.query.filter_by(id = review_id).first()
    form['csrf_token'].data = request.cookies['csrf_token']
    db.session.delete(review)
    db.session.commit()
    return "Successfully deleted."
