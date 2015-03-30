from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from service import db

class Record( db.Model ):
    __tablename__ = "records"
    id = Column( String, primary_key=True )
    name = Column( String )
    quantity = Column( Integer )

    def __init__( self, id, name, quantity ):
        self.id = id
        self.name = name
        self.quantity = quantity
