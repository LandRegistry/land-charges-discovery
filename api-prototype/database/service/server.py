from flask import Response, request, url_for
from service.model import LandCharge
from service import app, session
import json
import logging
import datetime
from sqlalchemy import *


@app.route('/', methods=['GET'])
def healthcheck():
    logging.info("healthcheck called")
    return Response("All OK", status=200)


@app.route('/search_all', methods=['GET'])
def get_lc():
    logging.info("search_all called")
    array = session.query(LandCharge).all()

    print(array)

    returns = []
    for item in array:
        returns.append(item.serialize())

    return Response(json.dumps(returns), status=200, mimetype='application/json')


@app.route('/search_name', methods=['POST'])
def get_name():
    logging.info("search_name called")
    json_data = request.get_json(force=True)

    json_data['name'] = json_data['name'].upper()
    array = session.query(LandCharge).filter_by(name=json_data['name']).all()

    returns = []
    for item in array:
        returns.append(item.serialize())

    return Response(json.dumps(returns), status=200, mimetype='application/json')


@app.route('/register', methods=['POST'])
def post_lc():
    logging.info("register called")
    if request.headers['Content-Type'] != "application/json":
        return Response(status=415)  # 415 (Unsupported Media Type)

    json_data = request.get_json(force=True)
    json_data['nature'] = json_data['nature'].upper()
    json_data['name'] = json_data['name'].upper()
    json_data['address'] = json_data['address'].upper()
    now = datetime.datetime.now()

    # write to the database
    item = LandCharge(nature=json_data['nature'], date=now.strftime("%d/%m/%Y"), name=json_data['name'],
                      address=json_data['address'])
    session.add(item)
    session.commit()

    # now write to the data files so that any inserts will remain when VM next brought up
    file = open("syt_nature.txt", "a")  # opens file
    file.write(json_data['nature'] + '\n')
    file.close()

    charge_data = json.loads(open('syt_data.json').read())

    charge_data['data'].append(
        {"name": json_data['name'], "address": json_data['address'], "nature": json_data['nature'],
         "date": "30.01.1908"})
    file = open("syt_data.json", "w")
    file.write(json.dumps(charge_data))

    # Return a 201 (Created) response, with the new item in the
    # response body.
    response = Response(status=201)
    return response

