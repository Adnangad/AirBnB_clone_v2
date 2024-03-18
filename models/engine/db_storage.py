from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
import sys
import os

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
        result = {}
        clas = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        if cls is None:
            query_cl = clas
        elif isinstance(cls, str):
            query_cl = [cls]
        else:
            query_cl = [cls.__name__]

        for clas_name in query_cl:
            clas_objects = self.__session.query(eval(clas_name)).all()
            for obj in clas_objects:
                k = f"{clas_name}.{obj.id}"
                result[k] = obj
        return result

    def new(self, obj):
        """Ads object to a databas."""
        self.session.add(obj)

    def save(self):
        """Commits changes to the database."""
        self.session.commit()

    def delete(self, obj=None):
        """Deletes obj from database."""
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        """Creates ll tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session()
