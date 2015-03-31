# Extremely noddy.

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()


class LandCharge(Base):
    __tablename__ = 'landcharge'
    id = Column(Integer, primary_key=True)
    chargee = Column(String, nullable=False)
    nature = Column(String, nullable=False)


class Application(Base):
    __tablename__ = 'application'
    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False)
    charge_id = Column(Integer, ForeignKey('landcharge.id'))
    land_charge = relationship(LandCharge)


engine = create_engine('postgresql://discotype:discotype@localhost/discotype')
Base.metadata.create_all(engine)

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

charges = [
    LandCharge(chargee="Bob Howard", nature="PAB"),
    LandCharge(chargee="Random Name", nature="PAB"),
    LandCharge(chargee="Bob Howard", nature="WOB")
]

applications = [
    Application(status="complete", land_charge=charges[0]),
    Application(status="cancelled", land_charge=charges[1]),
    Application(status="pending", land_charge=charges[2])
]

for item in charges:
    session.add(item)
session.commit()

for item in applications:
    session.add(item)
session.commit()

