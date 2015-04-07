from flask import Response, request, render_template
import requests
import logging
from client import app
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
            logging.log("Received 201")
            data = {
                "message": "Register complete"
            }
            return Response(json.dumps(data), status=201, mimetype='application/json')
        else:
            logging.error("Recieved " + response.status_code)
            return Response(response.status_code)


@app.route('/index', methods=['GET'])
def index():
    logging.info("index called")
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    logging.info("search called")
    forename_input = request.form['forename']
    surname_input = request.form['surname']


    #  Check Inputs
    if forename_input=="" and surname_input=="":
        print("please complete all fields")
        forename = 'Missing forename'
        surname = 'Missing surname'
        return render_template('index.html', forename_error=forename, surname_error=surname)
    elif forename_input=="":
        forename = 'Missing forename'
        return render_template('index.html', forename_error=forename, surname=surname_input)
    elif surname_input=="":
        surname = 'Missing surname'
        return render_template('index.html', surname_error=surname, forename=forename_input)
    else:
        # Call rest service to do search

        url = 'http://10.0.2.2:5001/search_name'
        data = {
            'name': request.form['forename'] + " " + request.form['surname']
        }
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json.dumps(data), headers=headers)

        print(json.dumps(response.json()))

    return render_template('index.html', results=response.json(), forename=forename_input, surname=surname_input )
logging.info("API started")