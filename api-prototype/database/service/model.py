from sqlalchemy import Column, Integer, String, ForeignKey
from service import Base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


class LandCharge(Base):
    __tablename__ = 'landcharge'
    id = Column(Integer, primary_key=True)
    nature = Column(String, nullable=False)
    date = Column(String, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)


    def serialize(self):
        return {
            'id': self.id,
            'nature': self.nature,
            'date': self.date,
            'name': self.name,
            'address': self.address
        }

engine = create_engine('postgresql://discotype:discotype@localhost/discotype')
Base.metadata.create_all(engine)


