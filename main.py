#!/usr/bin/env python
# coding=utf-8

import sys
from flask import Flask, request, jsonify
import simplejson as json
from config import tokens
app = Flask(__name__)


api_list = {
        'api/dns': u'get dns',
        'api/update': u'update domain information',
}

code = "200"
message = "success"
data = "ok"

response = {
    'status_code': code,
    "msg": message,
    "data": data
}
@app.route("/", methods = ['GET', 'POST'])
def index():
    return jsonify(api_list)

@app.route("/api/dns", methods=['GET', 'POST'])
def dns():
    msg = request.json
    token  = msg['token']
    ip = request.remote_addr
    if token in tokens:
        return jsonify(response)

@app.route("/api/update", methods=['GET', 'POST'])
def update():
    pass


if __name__ == '__main__':
    app.run(debug=True)



