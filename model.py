__author__ = 'Administrator'
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()



Base.metadata.create_all(engine)
