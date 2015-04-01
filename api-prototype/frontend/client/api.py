from flask import Response, request
import requests
from client import app
import json


@app.route('/', methods=['GET'])
def healthcheck():
    return Response(status=200)


@app.route('/b2b_register', methods=['POST'])
def process():
    if request.headers[ 'Content-Type' ] != "application/json":
        return Response( status=415 ) # 415 (Unsupported Media Type)
    else:
        json_data = request.get_json( force=True )

        url = 'http://10.0.2.2:8070/register'

        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json.dumps(json_data), headers=headers)

        if response.status_code == 201:
            data = {
                "message": "Register complete"
            }
            return Response(json.dumps(data), status=201, mimetype='application/json')
        else:
            print(response.status_code)
            return Response(response.status_code)


