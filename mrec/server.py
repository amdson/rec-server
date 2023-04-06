from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/query/<user_id>', methods = ['GET', 'POST'])
@cross_origin(origin="*", headers=["Content-Type"])
def user(user_id):
    if request.method == 'GET':
        """return the information for <user_id>"""
        return "POST requests only"
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.form # a multidict containing POST data
        response_body = {"user_id": user_id, 
            "media_data": [{"title": "Harry Potter and the Sorcerer's Stone", "media_id": 2}, 
                        {"title": "Redwall", "media_id": 3}]
        }
        print(data)
        return response_body

@app.route("/update")
def update():
    return "<p>Hello, World!</p>"