#!/usr/bin/env python
# coding=utf-8


import os
import sys
import dns.query
import dns.update
import re
from config import suffix
server = '172.16.3.131'

#reverse the ip and return
def reverseIP(s):
    pass

#get dns (support by ip and hostname)
def getDns(s):
    pass

#get ip by hostname
def getIpByHost(hostname):
    pass

#get hostname by ip
def getHostByIp(ip):
    pass

#get dns by ip and check by hostname(ip<-->hostname，return True)
def getDnsIp(ip , hostname):
    pass

def getAddIpAddrCmd(ip, host, ttl, zone):
    update = dns.update.Update(zone)
    update.add(host, ttl, 'A', ip)
    response = dns.query.tcp(update, server)
    return response

def getAddPTRCmd(rip, host, ttl, zone):
    update = dns.update.Update(zone)
    update.add(host, ttl, 'PTR', rip)
    response = dns.query.tcp(update, server)
    return response

def getDelIpAddrCmd(host, ip, ttl, zone):
    update = dns.update.Update(zone)
    update.delete(host, ttl, 'A', ip)
    response = dns.query.tcp(update, server)
    return response

def getDelPTRCmd(rip, host, ttl, zone):
    update = dns.update.Update(zone)
    update.delete(rip, ttl, 'PTR', host)
    response = dns.query.tcp(update, server)
    return response

def getAddRecordCmd(record):
    host = record['domain']
    ip = record['ip']
    a_zone = 'xiaojukeji.com'
    ptr_zone= ''
    msg = checkAddRecord(record)
    if msg[0] is not True:
        return msg
    getAddIpAddrCmd(host, ip, a_zone)
    getAddPTRCmd(host, ip, ptr_zone)
    return "success"

def getDelRecordCmd(record):
    host = record['domain']
    ip = record['ip']
    a_zone = 'xiaojukeji.com'
    ptr_zone= ''
    msg = checkDelRecord(record)
    if msg[0] is not True:
        return msg
    getDelIpAddrCmd(host, ip, a_zone)
    getDelPTRCmd(host, ip, ptr_zone)
    return "success"
    

#check add record (check ip/hostname and check dns by ip and hostname)
def checkAddRecord(record):
    if re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', record['ip']) is None:
        return [ 'False', 'invaild ip {0}'.format(record['ip'])]
    if re.findall(r'', record['domain']) is None:
        return [ 'False' ,'invaild new doamin {0}'.format(record['domain'])]

    return True

#check del record
def checkDelRecord(record):
    if re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', record['ip']) is None:
        return [ 'False', 'invaild ip {0}'.format(record['ip'])]
    if re.findall(r'', record['domain']) is None:
        return [ 'False' ,'invaild new doamin {0}'.format(record['domain'])]

    return True

#add the record (by check and add)
def addRecord(record):
#    err = checkAddRecord(record)
#    if err[0] is not True:
#        return err[1]

    result = getAddRecordCmd(record)
    return result

    

#del the record (by check and del)
def delRecord(record):
#    err = checkAddRecord(record)
#    if err[0] is not True:
#        return err[1]

    result = getAddRecordCmd(record)
    return result
