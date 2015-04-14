from flask import Response, request, render_template
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
    logging.info("GOT: " + r.status_code.__str__())
    return Response("Recieved", status=r.status_code)


@app.route('/b2b_postman', methods=['POST'])
def postman():
    logging.info("b2b_postman called")
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

@app.route('/insolvency', methods=['GET'])
def insolvency():
    logging.info("insolvency called")
    return render_template('insolvency.html')


@app.route('/b2b_register', methods=['POST'])
def process():
    logging.info("b2b_register called")
    name_input = request.form['name']
    nature_input = request.form['nature']
    address_input = request.form['address']
    name = 'Missing name'
    nature = 'Missing nature'
    address = 'Missing address'

    #  Check Inputs
    if name_input=="" and nature_input=="" and address_input=="":
        #print("please complete all fields")
        return render_template('insolvency.html', name_error=name, nature_error=nature, address_error=address)
    elif name_input=="" and nature_input=="":
        return render_template('insolvency.html', name_error=name, nature_error=nature)
    elif name_input=="" and address_input=="":
        return render_template('insolvency.html', name_error=name, address_error=address)
    elif nature_input== "" and address_input=="":
        return render_template('insolvency.html', nature_error=nature, address_error=address)
    else:
        logging.info("past if statements")
        url = 'http://10.0.2.2:5001/register'
        data={
            'name': request.form['name'],
            'address': request.form['address'],
            'nature': request.form['nature']
        }

        print(data)

        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json.dumps(data), headers=headers)

        if response.status_code == 201:
            logging.info("Received 201")
        else:
            logging.error("Recieved " + response.status_code)
            return Response(response.status_code)

    return render_template('insolvency.html', results="Registration Complete")

