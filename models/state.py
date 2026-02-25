#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class for representing states in the HBNB project."""
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", back_populates="state", cascade="all, delete-orphan"
        )
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a state object."""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Return list of City objects linked to this State."""
            from models import storage
            from models.city import City
            return [
                city for city in storage.all(City).values()
                if city.state_id == self.id
            ]
