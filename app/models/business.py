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
    country = db.Column(db.String(25),nullable=True)
    zip = db.Column(db.String(10),nullable=False)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    name = db.Column(db.String(255))
    description = db.Column(db.String(2500))
    price = db.Column(db.String,nullable=False)
    phone_number = db.Column(db.String(15),nullable=False)
    business_type = db.Column(db.String(25),nullable=False)
    monOpen = db.Column(db.String(50),nullable=False)
    tueOpen = db.Column(db.String(50),nullable=False)
    wedOpen = db.Column(db.String(50),nullable=False)
    thuOpen = db.Column(db.String(50),nullable=False)
    friOpen = db.Column(db.String(50),nullable=False)
    satOpen = db.Column(db.String(50),nullable=False)
    sunOpen = db.Column(db.String(50),nullable=False)
    monClose = db.Column(db.String(50),nullable=False)
    tueClose = db.Column(db.String(50),nullable=False)
    wedClose = db.Column(db.String(50),nullable=False)
    thuClose = db.Column(db.String(50),nullable=False)
    friClose = db.Column(db.String(50),nullable=False)
    satClose = db.Column(db.String(50),nullable=False)
    sunClose = db.Column(db.String(50),nullable=False)
    site = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),server_onupdate=db.func.now())

    # Relations
    users = db.relationship("User",back_populates="businesses")
    business_images = db.relationship("BusinessImage", back_populates="business", cascade="all, delete")
    reviews = db.relationship("Review", back_populates="business", cascade="all, delete")

    def to_dict_review(self):
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
            "monOpen": self.monOpen,
            "tueOpen": self.tueOpen,
            "wedOpen": self.wedOpen,
            "thuOpen": self.thuOpen,
            "friOpen": self.friOpen,
            "satOpen": self.satOpen,
            "sunOpen": self.sunOpen,
            "monClose": self.monClose,
            "tueClose": self.tueClose,
            "wedClose": self.wedClose,
            "thuClose": self.thuClose,
            "friClose": self.friClose,
            "satClose": self.satClose,
            "sunClose": self.sunClose,
            "site": self.site,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user": self.users.to_dict()
        }

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
            "monOpen": self.monOpen,
            "tueOpen": self.tueOpen,
            "wedOpen": self.wedOpen,
            "thuOpen": self.thuOpen,
            "friOpen": self.friOpen,
            "satOpen": self.satOpen,
            "sunOpen": self.sunOpen,
            "monClose": self.monClose,
            "tueClose": self.tueClose,
            "wedClose": self.wedClose,
            "thuClose": self.thuClose,
            "friClose": self.friClose,
            "satClose": self.satClose,
            "sunClose": self.sunClose,
            "site": self.site,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user": self.users.to_dict(),
            "reviews": [review.to_dict() for review in self.reviews],
            "images": [image.to_dict() for image in self.business_images]
        }
