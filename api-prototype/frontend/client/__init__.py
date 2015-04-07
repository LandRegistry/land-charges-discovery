from flask import Flask
import logging
import os

app = Flask(__name__)
app.config.from_object(os.environ.get('SETTINGS'))
logging.basicConfig(level=logging.DEBUG)
logging.info("started")