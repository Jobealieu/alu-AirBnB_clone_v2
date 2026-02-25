#!/usr/bin/python3
"""DBStorage module for database storage using SQLAlchemy."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Handles storage of hbnb models using SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object."""
        HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")
        HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
        HBNB_ENV = os.getenv("HBNB_ENV")
        db = "mysql+mysqldb://{}:{}@{}/{}?charset=utf8mb4".format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST, HBNB_MYSQL_DB
        )
        self.__engine = create_engine(db, pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        if cls is not None:
            objs_dict = {
                "{}.{}".format(obj.__class__.__name__, obj.id): obj
                for obj in self.__session.query(cls)
            }
            return objs_dict
        else:
            classes = [State, Review, User, Place, City]
            objs_dict = {}
            for item in classes:
                for obj in self.__session.query(item):
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objs_dict[key] = obj
            return objs_dict

    def new(self, obj):
        """Add the object to the current database session."""
        if self.__session is not None:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        if self.__session is not None:
            self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if not None."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize the session."""
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove on the private session attribute."""
        self.__session.remove()
