from flask import Response
from service.model import LandCharge, Application
from service import app, session
import json


@app.route('/', methods=['GET'])
def healthcheck():
    return Response(status=200)


@app.route('/lc', methods=['GET'])
def get_lc():
    array = session.query(LandCharge).all()

    returns = []
    for item in array:
        returns.append(item.serialize())

    return Response(json.dumps(returns), status=200, mimetype='application/json')