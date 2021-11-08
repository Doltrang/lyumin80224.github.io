from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,Enum
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///nobel_prize.db',echo=True)
base = declarative_base()

class Winner(base):
    __tablename__ = 'winners'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male','female'))

base.metadata.create_all(engine)