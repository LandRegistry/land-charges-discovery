import os


class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
