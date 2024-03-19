#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os
import models

place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """Contains class place."""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="place")
        amenities = relationship(
                'Amenity',
                secondary=place_amenity,
                back_populates='place_amenity',
                viewonly=False)
    else:
        @property
        def review(self):
            ls = []
            temp = models.db_storage.all(Review)
            for review in temp.values():
                if review.place_id == self.id:
                    ls.append(review)
            return ls
        @property
        def amenities(self):
            ls = []
            ls.append(self.amenity_ids)
            return ls
        
        @amenities.setter
        def amenities(self, obj=None):
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
