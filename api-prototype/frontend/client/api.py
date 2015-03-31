from flask import Response
import requests
from client import app


@app.route('/', methods=['GET'])
def healthcheck():
    return Response(status=200)


@app.route('/remote', methods=['GET'])
def remote_healthcheck():
    r = requests.get('http://10.0.2.2:8080/')
    return Response(status=r.status_code)