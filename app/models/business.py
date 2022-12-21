from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Business(db.Model):
    __tablename__ = "business"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    address = db.Column(db.String(255),nullable=False)
    city = db.Column(db.String(25),nullable=False)
    state = db.Column(db.String(25),nullable=False)
    country = db.Column(db.String(25),nullable=False)
    zip = db.Column(db.String(10),nullable=False)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    name = db.Column(db.String(255))
    description = db.Column(db.String(2500),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    phone_number = db.Column(db.String(15),nullable=False)
    business_type = db.Column(db.String(25),nullable=False)
    business_hour = db.Column(db.String(50),nullable=False)
    site = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),server_onupdate=db.func.now())

    # Relations
    users = db.relationship("User",back_populates="business")
    business_images = db.relationship("BusinessImages", back_populates="business", cascade="all, delete")
    business_reviews = db.relationship("BusinessReviews", back_populates="business", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "zip": self.zip,
            "lat": self.lat,
            "lng": self.lng,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "phone_number": self.phone_number,
            "business_type": self.business_type,
            "business_hour": self.business_hour,
            "site": self.site
            "create_at": self.create_at,
            "updated_at": self.updated_at
        }
