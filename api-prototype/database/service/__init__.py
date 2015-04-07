from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os

app = Flask( __name__ )
# db = SQLAlchemy( app )
app.config.from_object( os.environ.get( 'SETTINGS' ) )

Base = declarative_base()

engine = create_engine('postgresql://discotype:discotype@localhost/discotype')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
logging.basicConfig(level=logging.DEBUG)
logging.info("started")