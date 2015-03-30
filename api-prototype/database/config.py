import os

class Config( object ):
    DEBUG = False

class DevelopmentConfig( Config ):
    SQLALCHEMY_DATABASE_URI = 'postgresql://discotype:discotype@localhost/discotype'
    DEBUG = True
