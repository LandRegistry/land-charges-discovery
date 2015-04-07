from flask import Response, request, url_for
from service.model import LandCharge
from service import app, session
import json
import logging
from sqlalchemy import *

@app.route('/', methods=['GET'])
def healthcheck():
    logging.info("healthcheck called")
    return Response(status=200)


@app.route('/search_all', methods=['GET'])
def get_lc():
    logging.info("search_all called")
    array = session.query(LandCharge).all()

    returns = []
    for item in array:
        returns.append(item.serialize())


    return Response(json.dumps(returns), status=200, mimetype='application/json')

@app.route('/search_name', methods=['POST'])
def get_name():
    logging.info("search_name called")
    json_data = request.get_json( force=True )


    array = session.query(LandCharge).filter_by(name= json_data[ 'name' ]).all()


    returns = []
    for item in array:
        returns.append(item.serialize())

    return Response(json.dumps(returns), status=200, mimetype='application/json')



@app.route('/register', methods=['POST'])
def post_lc():
    logging.info("register called")
    if request.headers[ 'Content-Type' ] != "application/json":
        return Response( status=415 ) # 415 (Unsupported Media Type)

    json_data = request.get_json( force=True )

    item = LandCharge(nature= json_data[ 'nature'], date= "20.03.2105", name= json_data[ 'name' ], address= json_data[ 'address' ])
    session.add(item)
    session.commit()



# Return a 201 (Created) response, with the new item in the
# response body.
    response = Response( status=201 )
    return response

