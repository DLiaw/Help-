from flask import Flask, jsonify, Blueprint, redirect, request
from ..models import db, User, Review, Business, ReviewImage, BusinessImage
from ..forms import BusinessForm, BusinessImageForm, ReviewForm, ReviewImageForm, SignUpForm, LoginForm
from flask_login import login_required, current_user
from app.api.auth_routes import validation_errors_to_error_messages
business_routes = Blueprint("business", __name__)



## Get all businesses
@business_routes.route('/',methods=['GET'])
def get_all_business():
    businesses = Business.query.all()
    return {'businesses': [business.to_dict() for business in businesses]}


## Create a business
@business_routes.route('/new',methods=['POST'])
@login_required
def create_business():
    form = BusinessForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_business = Business(
            owner_id = form.data['owner_id'],
            address = form.data['address'],
            city = form.data['city'],
            state = form.data['state'],
            zip = form.data['zip'],
            name = form.data['name'],
            price = form.data['price'],
            phone_number = form.data['phone_number'],
            business_type = form.data['business_type'],
            monOpen = form.data['monOpen'],
            tueOpen = form.data['tueOpen'],
            wedOpen = form.data['wedOpen'],
            thuOpen = form.data['thuOpen'],
            friOpen = form.data['friOpen'],
            satOpen = form.data['satOpen'],
            sunOpen = form.data['sunOpen'],
            monClose = form.data['monClose'],
            tueClose = form.data['tueClose'],
            wedClose = form.data['wedClose'],
            thuClose = form.data['thuClose'],
            friClose = form.data['friClose'],
            satClose = form.data['satClose'],
            sunClose = form.data['sunClose'],
            site = form.data['site']
        )
        db.session.add(new_business)
        db.session.commit()
        return new_business.to_dict()
    return {"errors": form.errors}, 401

## Update business by id
@business_routes.route('/<int:id>/edit',methods=['PUT'])
@login_required
def update_business(id):
    updated_business = Business.query.filter_by(id = id).first()
    form = BusinessForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        setattr(updated_business,'address', form.data['address'])
        setattr(updated_business,'city', form.data['city'])
        setattr(updated_business,'state', form.data['state'])
        setattr(updated_business,'zip', form.data['zip'])
        setattr(updated_business,'name', form.data['name'])
        setattr(updated_business,'price', form.data['price'])
        setattr(updated_business,'phone_number', form.data['phone_number'])
        setattr(updated_business,'business_type', form.data['business_type'])
        setattr(updated_business,'monOpen', form.data['monOpen'])
        setattr(updated_business,'tueOpen', form.data['tueOpen'])
        setattr(updated_business,'wedOpen', form.data['wedOpen'])
        setattr(updated_business,'thuOpen', form.data['thuOpen'])
        setattr(updated_business,'friOpen', form.data['friOpen'])
        setattr(updated_business,'satOpen', form.data['satOpen'])
        setattr(updated_business,'sunOpen', form.data['sunOpen'])
        setattr(updated_business,'monClose', form.data['monClose'])
        setattr(updated_business,'tueClose', form.data['tueClose'])
        setattr(updated_business,'wedClose', form.data['wedClose'])
        setattr(updated_business,'thuClose', form.data['thuClose'])
        setattr(updated_business,'friClose', form.data['friClose'])
        setattr(updated_business,'satClose', form.data['satClose'])
        setattr(updated_business,'sunClose', form.data['sunClose'])
        setattr(updated_business,'site', form.data['site'])
        db.session.commit()
        res = updated_business.to_dict()
        return res
    if form.errors:
        return {"errors": form.errors}, 401

## Get business by id
@business_routes.route('/<int:id>',methods=['GET'])
def business_by_id(id):
    business = Business.query.get(id)
    return business.to_dict()

## Delete a business
@business_routes.route('/<int:id>',methods=['DELETE'])
@login_required
def delete_business(id):
    business = Business.query.get(id)
    db.session.delete(business)
    db.session.commit()
    return "Successfully deleted."

## Create review for business
@business_routes.route('/<int:id>/reviews',methods=['POST'])
@login_required
def review_business(id):
    user = current_user.id
    business = Business.query.get(id)
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if not business:
        return "Business not found"
    if business:
        if form.validate_on_submit():
            review = Review(
                user_id = user,
                business_id = business.id,
                review = form.data['review'],
                stars = form.data['stars']
            )
            db.session.add(review)
            db.session.commit()
            return review.to_dict()
        if form.errors:
            return {"errors": validation_errors_to_error_messages(form.errors)}, 401

## Add image for business
@business_routes.route('/<int:id>/images',methods=['POST'])
@login_required
def business_image(id):
    form = BusinessImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        image = BusinessImageForm(
            business_id = form.data['business_id'],
            business_image = form.data['business_image'],
            preview = form.data['preview']
        )
        db.session.add(image)
        db.session.commit()
        return image.to_dict()
