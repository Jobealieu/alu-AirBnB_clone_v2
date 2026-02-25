#!/usr/bin/python3
"""BaseModel module for the AirBnB clone project."""
from sqlalchemy import Column, String, DateTime
from sqlalchemy import ForeignKey
try:
    from sqlalchemy.orm import declarative_base
except ImportError:
    from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime
import models


Base = declarative_base()


class BaseModel:
    """BaseModel class that defines common methods and attributes."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class."""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("updated_at", "created_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at and save the instance to storage."""
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        instance_dict = self.__dict__.copy()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in instance_dict.keys():
            del instance_dict["_sa_instance_state"]
        return instance_dict

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)
