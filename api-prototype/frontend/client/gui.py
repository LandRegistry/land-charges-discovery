from flask import render_template, request
from client import app
import requests
import json


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():

    forename_input = request.form['forename'];
    surname_input = request.form['surname'];
    alternative_input = request.form['alternative']


    #  Check Inputs
    if forename_input=="" and surname_input=="" and alternative_input=="":
        #print("please complete all fields")
        forename = 'Missing forename'
        surname = 'Missing surname'
        altname = 'Missing complex name'
        return render_template('index.html', forename_error=forename, surname_error=surname, altname_error=altname)
    elif forename_input=="" and alternative_input=="":
        forename = 'Missing forename'
        return render_template('index.html', forename_error=forename, surname=surname_input)
    elif surname_input=="" and alternative_input=="":
        surname = 'Missing surname'
        return render_template('index.html', surname_error=surname, forename=forename_input)
    else:
        # Call rest service to do search

        url = 'http://10.0.2.2:8070/search_name'
        if alternative_input=="":
            data = {
                'name': request.form['forename'] + " " + request.form['surname']
            }
        else:
            data = {
                'name': request.form['alternative']
            }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json.dumps(data), headers=headers)

        #print(json.dumps(response.json()))

    return render_template('index.html', results=response.json(), forename=forename_input, surname=surname_input, alternative=alternative_input )


