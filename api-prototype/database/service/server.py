from flask import Response, request, url_for
from service.model import LandCharge
from service import app, session
import json
import datetime
from sqlalchemy import *

@app.route('/', methods=['GET'])
def healthcheck():
    return Response(status=200)


@app.route('/search_all', methods=['GET'])
def get_lc():
    array = session.query(LandCharge).all()

    returns = []
    for item in array:
        returns.append(item.serialize())


    return Response(json.dumps(returns), status=200, mimetype='application/json')

@app.route('/search_name', methods=['POST'])
def get_name():
    json_data = request.get_json( force=True )

    json_data[ 'name' ] = json_data[ 'name' ].upper()
    array = session.query(LandCharge).filter_by(name= json_data[ 'name' ]).all()

    returns = []
    for item in array:
        returns.append(item.serialize())

    return Response(json.dumps(returns), status=200, mimetype='application/json')



@app.route('/register', methods=['POST'])
def post_lc():
    if request.headers[ 'Content-Type' ] != "application/json":
        return Response( status=415 ) # 415 (Unsupported Media Type)

    json_data = request.get_json( force=True )
    json_data[ 'nature' ] = json_data[ 'nature' ].upper()
    json_data[ 'name' ] = json_data[ 'name' ].upper()
    json_data[ 'address' ] = json_data[ 'address' ].upper()
    now = datetime.datetime.now()

    #write to the database
    item = LandCharge(nature= json_data[ 'nature'], date= now.strftime("%d/%m/%Y"), name= json_data[ 'name' ], address= json_data[ 'address' ])
    session.add(item)
    session.commit()


    charge_data = json.loads(open('syt_data.json').read())

    charge_data['data'].append({"name": json_data['name'], "address": json_data['address'], "nature": json_data['nature'], "date": "30.01.1908"} )
    file = open("syt_data.json","w")
    file.write(json.dumps(charge_data))


# Return a 201 (Created) response, with the new item in the
# response body.
    response = Response( status=201 )
    return response

