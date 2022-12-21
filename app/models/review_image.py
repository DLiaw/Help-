from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class ReviewImage(db.Model):
    __tablename__ = "review_images"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=False)
    review_image = db.Column(db.String(500),nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),server_onupdate=db.func.now())

    # Relations
    reviews = db.relationship("Review", back_populates="review_images")

    def to_dict(self):
        return {
            'id': self.id,
            'review_id': self.review_id,
            'review_image': self.review_image,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
