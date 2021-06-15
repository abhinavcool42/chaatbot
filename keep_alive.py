from flask import Flask
from threading import Thread
#from main.py import chatbot
from flask import jsonify
from flask import request
from chaatbot import chatbot
#from flask_restful import Resource, Api, reqparse
#import pandas as pd
#import ast

app = Flask('')
#api = Api(app)

'''
class chaat(Resource):
    def get(self):
        data = pd.read_csv('users.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

api.add_resource(chaat, '/chaat')
'''

@app.route('/api', methods=['GET'])
def api_id():
 temp1=request.args.get("msg")
 print(temp1)
 temp2=chatbot.get_response(temp1)
 print(temp2)
 #return jsonify(temp)
 temp3=str(temp2)
 return temp3 

@app.route('/')
def home():
 return "Yes"

def run():
  app.run(host='0.0.0.0',port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    app.run(ssl_context='adhoc',threaded=True)

'''
t = Thread(target=run)
t.start()
app.run(host="0.0.0.0", port=8080)
'''