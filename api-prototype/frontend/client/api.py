from flask import Response, request
import requests
import logging
from client import app
from client.gui import app
import json


@app.route('/', methods=['GET'])
def healthcheck():
    logging.info("healthcheck called")
    return Response("OK",status=200)

@app.route( '/remote', methods=['GET'])
def remote_healthcheck():
    logging.info("remote healthcheck called")
    r = requests.get('http://10.0.2.2:5001/')
    return Response("Recieved", status=r.status_code)


@app.route('/b2b_register', methods=['POST'])
def process():
    logging.info("b2b_register called")
    if request.headers[ 'Content-Type' ] != "application/json":
        return Response( status=415 ) # 415 (Unsupported Media Type)
    else:
        json_data = request.get_json( force=True )

        url = 'http://10.0.2.2:5001/register'

        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json.dumps(json_data), headers=headers)

        if response.status_code == 201:
            logging.info("Received 201")
            data = {
                "message": "Register complete"
            }
            return Response(json.dumps(data), status=201, mimetype='application/json')
        else:
            logging.error("Recieved " + response.status_code)
            return Response(response.status_code)

