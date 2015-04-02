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

nature_file = open("syt_nature.txt","r") #opens file
nature_list = []
for line in nature_file:
    nline = line.replace("\n"," ")
    line = nline.strip()
    nature_list.append(line)
nature_file.close()

date_file = open("syt_date.txt","r") #opens file
date_list = []
for line in date_file:
    nline = line.replace("\n"," ")
    line = nline.strip()
    date_list.append(line)
date_file.close()

name_file = open("syt_name.txt","r") #opens file
name_list = []
for line in name_file:
    nline = line.replace("\n"," ")
    line = nline.strip()
    name_list.append(line)
name_file.close()

addr_file = open("syt_address.txt","r") #opens file
addr_list = []
for line in addr_file:
    nline = line.replace("\n"," ")
    line = nline.strip()
    addr_list.append(line)
addr_file.close()

list_len = len(nature_list)

count = 0
charges = []
while (count < list_len):
    charges.append(LandCharge(nature=nature_list[count],date=date_list[count],name=name_list[count],address=addr_list[count]))
    count = count + 1

for item in charges:
    session.add(item)
session.commit()

