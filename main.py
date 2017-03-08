#!/usr/bin/env python
# coding=utf-8

import sys
from flask import Flask, request, jsonify

app = Flask(__name__)


api_list = {
        'api/dns': u'get dns',
        'api/update': u'update domain information',
}

@app.route("/", methods = ['GET', 'POST'])
def index():
    return jsonify(api_list)

@app.route("/api/dns", methods=["GET", "POST"])
def dns():
    pass

@app.route("/api/update", methods=["GET", "POST"])
def update():
    pass


if __name__ == '__main__':
    app.run(debug=True)



