#!/usr/bin/env python
# coding=utf-8


import os
import sys
import dns.query
import dns.update
import re
from config import asuffix, psuffix
server = '172.16.3.131'

def gethost(domain, a_zone):
    c= ""
    test = domain.split('.')
    for i in reversed(range(len(test))):
        c = test[i] + '.' + c
        if c == a_zone:
            return test[i-1]

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
def getDnsIp(ip, hostname):
    pass

def getAddIpAddrCmd(host, ip, ttl, zone):
    update = dns.update.Update(zone)
    update.add(host, ttl, 'A', ip)
    response = dns.query.tcp(update, server)
    return response

def getAddPTRCmd(host, rip, ttl, zone):
    update = dns.update.Update(zone)
    update.add(rip, ttl, 'PTR', host)
    response = dns.query.tcp(update, server)
    return response

def getDelIpAddrCmd(host, ip, ttl, zone):
    update = dns.update.Update(zone)
    update.delete(host, ttl, 'A', ip)
    response = dns.query.tcp(update, server)
    return response

def getDelPTRCmd(host, rip, ttl, zone):
    update = dns.update.Update(zone)
    update.delete(rip, ttl, 'PTR', host)
    response = dns.query.tcp(update, server)
    return response

def getAddRecordCmd(record):
    ip = record['ip']
    rip = ('.').join(ip.split('.')[::-1]) + '.in-addr.arpa'
    a_zone = re.search(asuffix, record['domain'] + '.').group(0)
    ptr_zone = re.search(psuffix, rip).group(0)
    ttl = 60
    host = gethost(record['domain'], a_zone +'.')
    msg = checkAddRecord(record)
    if not msg[0]:
        return msg
    getAddIpAddrCmd(host, ip, ttl, a_zone)
    getAddPTRCmd(host, rip, ttl, ptr_zone)
    return "success"

def getDelRecordCmd(record):
    ip = record['ip']
    rip = ('.').join(ip.split('.')[::-1]) + '.in-addr.arpa'
    a_zone = re.search(asuffix + '.', record['domain'] +'.').group(0)
    ptr_zone= re.search(psuffix, rip).group(0)
    ttl = 60
    host = gethost(record['domain'], a_zone +'.')
    msg = checkDelRecord(record)
    if not msg[0]:
        return msg
    print host, ttl, ip , a_zone
    getDelIpAddrCmd(host, ip, ttl, a_zone)
    getDelPTRCmd(host, ip, ttl, ptr_zone)
    return "success"
    

#check add record (check ip/hostname and check dns by ip and hostname)
def checkAddRecord(record):
    if re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', record['ip']) is None:
        return ['False', 'invaild ip %s' % record['ip']]
    if re.findall(asuffix, record['domain']) is None:
        return ['False', 'invaild doamin %s' % record['domain']]

    return ['True',]

#check del record
def checkDelRecord(record):
    if re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', record['ip']) is None:
        return ['False', 'invaild ip %s' % record['ip']]
    if re.findall(psuffix, record['domain']) is None:
        return ['False', 'invaild doamin %s' % record['domain']]

    return ['True', ]

#add the record (by check and add)
def addRecord(record):
    err = checkAddRecord(record)
    if not err[0]:
        return err[1]
    result = getAddRecordCmd(record)
    return result

    

#del the record (by check and del)
def delRecord(record):
    err = checkAddRecord(record)
    print err
    if not err[0]:
        return err[1]

    result = getAddRecordCmd(record)
    return result
