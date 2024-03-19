#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import os

class State(BaseModel, Base):
    """This is a class state"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                cascade='all, delete, delete-orphan',
                          backref="state")
    else:
        @property
        def cities(self):
            ls = []
            temp = models.db_storage.all(City)
            for ct in temp.values():
                if ct.state_id == self.id:
                    ls.append(ct)
            return ls

