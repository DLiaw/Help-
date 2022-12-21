from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class BusinessImage(db.Model):
    __tablename__ = "business_images"

    if environment == "production"
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    business_image = db.Column(db.String(500),nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),server_onupdate=db.func.now())

    # Relations
    business = db.relationship("Business", back_populates="business_images")

    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'business_image': self.business_image,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
