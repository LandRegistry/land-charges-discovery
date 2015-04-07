# Extremely noddy.

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from sqlalchemy.orm import relationship

Base = declarative_base()


class LandCharge(Base):
    __tablename__ = 'landcharge'
    id = Column(Integer, primary_key=True)
    nature = Column(String, nullable=False)
    date = Column(String, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)


#class Application(Base):
#    __tablename__ = 'application'
#    id = Column(Integer, primary_key=True)
#    status = Column(String, nullable=False)
#    charge_id = Column(Integer, ForeignKey('landcharge.id'))
#    land_charge = relationship(LandCharge)


engine = create_engine('postgresql://discotype:discotype@localhost/discotype')
Base.metadata.create_all(engine)

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



charge_data = json.loads(open('syt_data.json').read())

charges=[]
for charge in charge_data['data']:
    charges.append(LandCharge(nature=charge['nature'],date=charge['date'],name=charge['name'],address=charge['address']))

for item in charges:
    session.add(item)
session.commit()

