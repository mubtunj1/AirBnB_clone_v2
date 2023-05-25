#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages the connection to the database
    and performs database operations."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage."""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, passwd, host, db),
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects of a given class from the database.

        Args:
            cls (class, optional): The class to query objects
            from. Defaults to None.

        Returns:
            dict: A dictionary of objects mapped by their key.
        """
        dic = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for cls in classes:
                query = self.__session.query(cls)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic

    def new(self, obj):
        """
        Add a new object to the database session.

        Args:
            obj: The object to add.
        """
        self.__session.add(obj)

    def save(self):
        """Commit the changes made in the current session to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the database session.

        Args:
            obj: The object to delete.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all database tables and create a new session."""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """Close the current session."""
        self.__session.close()
