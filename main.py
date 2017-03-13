#!/usr/bin/env python
# coding=utf-8

import sys
from flask import Flask, request, jsonify
import simplejson as json
from flask_json import FlaskJSON, JsonError, json_response, as_json
import handlers
app = Flask(__name__)
FlaskJSON(app)

api_list = {
        'api/dns': u'get dns',
        'api/update': u'update domain information',
}

@app.route("/", methods = ['GET', 'POST'])
def index():
    return jsonify(api_list)

@app.route("/api/dns", methods=['GET', 'POST'])
def dns():
    body = request.json
    ip = request.remote_addr
    data  = handlers.DNSHandler(ip, body)
    return jsonify(data)

@app.route("/api/update", methods=['GET', 'POST'])
def update():
    pass


if __name__ == '__main__':
    app.run(debug=True)



