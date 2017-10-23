import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DatabaseEngine:
    def __init__(self, **kwargs):
        self.__dbdialect = str()
        self.__dbdriver = str()
        self.__dbname = str()
        self.__dbhost = str()
        self.__username = str()
        self.__password = str()

        self.__base_dir = os.getcwd()

        self.__platform_system = str()

        self._check_parameters(kwargs)
        # Database Urls
        # http://docs.sqlalchemy.org/en/latest/core/engines.html
        if self.__dbdialect == 'sqlite':
            create_engine_msg = 'sqlite:///{}'.format(os.path.join(self.__base_dir, self.__dbname))

        elif self.__dbdialect == 'postgresql':
            create_engine_msg = 'postgres{}://{}:{}@{}/{}'\
                .format(self.__dbdriver, self.__username, self.__password, self.__dbhost, self.__dbname)

        else:
            print('No Dabase')

        self._engine = create_engine(create_engine_msg, convert_unicode=True, encoding='utf-8')
        self._session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self._engine))

    def get_engine(self):
        return self._engine

    def get_session(self):
        return self._session

    def _check_parameters(self, kwargs: dict):
        self.__base_dir = os.getcwd()

        if 'username' in kwargs:
            self.__username = kwargs['username']

        if 'password' in kwargs:
            self.__password = kwargs['password']

        if 'dbdialect' in kwargs:
            self.__dbdialect = kwargs['dbdialect']
        else:
            self.__dbdialect = 'sqlite'

        if 'dbdriver' in kwargs:
            self.__dbdriver = '+{}'.format(kwargs['dbdriver'])

        if 'dbhost' in kwargs:
            self.__dbhost = kwargs['dbhost']
        else:
            self.__dbhost = 'localhost'

        if 'dbname' in kwargs:
            self.__dbname = kwargs['dbname']
        else:
            self.__dbname = 'db.sqlite'
