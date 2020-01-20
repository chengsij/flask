import os
import sys
import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.before_request
def before_request():
    request_data = {}
    request_data['method'] = request.method
    request_data['endpoint'] = request.endpoint
    request_data['data'] = request.data
    request_data['headers'] = dict(request.headers)
    request_data['args'] = request.args
    print ("request headers: ")
    print (request.headers)


@app.after_request
def after_request(resp):
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Headers', 'Content-Type, X-Token')
    return resp


@app.route("/v3/hello", methods=['GET', 'PUT', 'POST'])
def hello():
    message = {}
    message['text'] = "Hello"
    message['status'] = "200"
    response = Response(json.dumps(message, indent=4), mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run('localhost', port=8087, debug=True)