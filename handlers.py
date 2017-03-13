#!/usr/bin/env python
# coding=utf-8

import os
import simplejson as json
import logging
from config import tokens, ips
from utils import addRecord, delRecord


#check the dns
def checkModDns(records):
    pass

#add the dns
def addDns(records):
    reason = addRecord(records)
    response = {
        "reason": "",
        "msg": "success",
        "status": "200"
    }
    return response

#del the dns
def delDns(records):
    reason = delRecord(records)
    response = {
        "reason": "",
        "msg": "success",
        "status": "200"

    }
    return response

#get the Hostname by ip
def getHostName(records):
    response = {
          "status": "success",
    }
    return response

#get the ip by Hostname
def getIp(records):
    response = {
          "status": "success",
    }
    return response


handler = {
    "ADD": addDns,
    "DEL": delDns,
    "GET_IP": getIp,
    "GET_HOS": getHostName
}


def UpdateHandler(w, req):
    pass

def DNSHandler(ip, data):

    #check remote ip and check token
    if ( ip not in ips ) or ( data['token'] not in tokens):
        return {
            "msg": "fail",
            "reason": "authorized fail because ip or token is error",
            "status": "403",
        }

    #handler
    msg = handler.get(data['opcode'])(data['records'])
    return msg
