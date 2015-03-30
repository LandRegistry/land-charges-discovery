from flask import Flask, Response
from service.model import Record
from service import app, db

@app.route( '/', methods=[ 'GET' ] )
def healthcheck():
    return Response( status=200 )
