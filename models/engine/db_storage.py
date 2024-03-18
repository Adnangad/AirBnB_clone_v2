from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from sqlalchemy.orm import scoped_session
import sys
import os
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """This class creates sessions and engines."""
    __engine = None
    __session = None
    
    def __init__(self):
        """Initializes variables."""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(os.getenv('HBNB_MYSQL_USER'),
                    os.getenv('HBNB_MYSQL_PWD'),
                    os.getenv('HBNB_MYSQL_HOST'),
                    os.getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on database sessions."""
        rez = {}
        if cls is None:
            for i in classes:
                data = self.__session.query(i)
                for item in data:
                    key = "{}.{}".format(type(item).__name__, item.id)
                rez[key] = item
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            data = self.__session.query(cls)
            for item in data:
                key = f"{type(item).__name__}.{item.id}"
                rez[key] = item
        return rez

    def new(self, obj):
        """Ads object to a databas."""
        self.__session.add(obj)

    def save(self):
        """Commits changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from database."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates ll tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session()
