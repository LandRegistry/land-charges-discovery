from sqlalchemy import Column, Integer, String, ForeignKey
from service import Base
from sqlalchemy.orm import relationship


class LandCharge(Base):
    __tablename__ = 'landcharge'
    id = Column(Integer, primary_key=True)
    chargee = Column(String, nullable=False)
    nature = Column(String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'chargee': self.chargee,
            'nature': self.nature
        }


class Application(Base):
    __tablename__ = 'application'
    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False)
    charge_id = Column(Integer, ForeignKey('landcharge.id'))
    land_charge = relationship(LandCharge)