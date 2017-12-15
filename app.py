from flask import Flask, request
import requests
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.secret_key = 'proseth123'
api = Api(app)

class SmsGateWay(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                            type=str,
                            required=True,
                            help='This field cannot be left blank!'
                            )
    parser.add_argument('password',
                            type=str,
                            required=True,
                            help='This field cannot be left blank!'
                            )
    parser.add_argument('device',
                            type=int,
                            required=True,
                            help='This field cannot be left blank!'
                            )
    parser.add_argument('number',
                            type=str,
                            required=True,
                            help='This field cannot be left blank!'
                            )
    parser.add_argument('message',
                            type=str,
                            required=True,
                            help='This field cannot be left blank!'
                            )

    # def get(self):
    #     data = Item.parser.parse_args()
    #     parameter = {'email': data['email'],'password': data['password']}
    #     response = requests.get('http://smsgateway.me/api/v3/messages',params=parameter)
    #     return {'item': item}, 200 if item else 404
    
    def post(self):
        
        data = SmsGateWay.parser.parse_args()
        parameter = {'email': data['email'],
        'password': data['password'], 
        'device': data['device'], 
        'number': data['number'],  
        'message': data['message']}

        response = requests.post('http://smsgateway.me/api/v3/messages/send',params=parameter)

        data_response = response.json()

        return data_response['success']

    
  

api.add_resource(SmsGateWay, '/smsgateway')

app.run(port = 5000, debug=True)
