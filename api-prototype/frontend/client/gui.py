from flask import render_template, request
from client import app
import requests
import json


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    #error = None

    if request.form['forename']=="" or request.form['surname']=="":
        print("please complete all fields")
        #error = 'Invalid username/password'
    else:


        url = 'http://10.0.2.2:8070/search_name'
        data = {
            'name': request.form['forename'] + " " + request.form['surname']
        }
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json.dumps(data), headers=headers)

        print(json.dumps(response.json()))

    return render_template('index.html', results=response.json() )
    #return render_template('index.html')
   # return render_template('login.html', error=error)

