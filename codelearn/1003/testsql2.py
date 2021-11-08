nobel_winners = [
{'category': 'Physics',
'name': 'Albert Einstein',
'nationality': 'Swiss',
'sex': 'male',
'year': 1921},
{'category': 'Physics',
'name': 'Paul Dirac',
'nationality': 'British',
'sex': 'male',
'year': 1933},
{'category': 'Chemistry',
'name': 'Marie Curie',
'nationality': 'Polish',
'sex': 'female',
'year': 1911}
]

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

    def __repr__(self):
        return '<Winner({},{},{})>'.format(self.name,self.category,self.year)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

winner_rows = [ Winner(**w) for w in nobel_winners]
session.add_all(winner_rows)
session.commit()