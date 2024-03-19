#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.place import place_amenity

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity)
