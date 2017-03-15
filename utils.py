#!/usr/bin/env python
# coding=utf-8


import os
import sys
import re
from config import suffix
from constants import NSUPDA
server = '172.16.3.131'

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

def getAddIpAddrCmd(host, ip, ttl):
    cmd = "echo $'server %s \nupdate add %s %d A %s\r\nsend \r\nquit\n' | nsupdate -t5 -v -k ./nsupdate.key -v" % (server, host, ttl, ip)
    result = os.system(cmd)
    return result

def getAddPTRCmd(host, rip, ttl):
    cmd = "echo $'server %s \nupdate add %s %d PTR  %s\r\nsend \r\nquit\n' | nsupdate -t5 -v -k ./nsupdate.key -v" % (server, rip, ttl, host)
    result = os.system(cmd)
    return result

def getDelIpAddrCmd(host, ip, ttl):
    cmd = "echo $'server %s \nupdate delete %s %d A %s\r\nsend \r\nquit\n' | nsupdate -t5 -v -k ./nsupdate.key -v" % (server, host, ttl, ip)
    result = os.system(cmd)
    return result

def getDelPTRCmd(host, rip, ttl):
    cmd = "echo $'server %s \nupdate delete %s %d PTR %s\r\nsend \r\nquit\n' | nsupdate -t5 -v -k ./nsupdate.key -v" % (server, rip, ttl, host)
    result = os.system(cmd)
    return result

def getAddRecordCmd(record):
    ip = record['ip']
    rip = ('.').join(ip.split('.')[::-1]) + '.in-addr.arpa'
    ttl = 60
    host = record['domain']
    msg = checkAddRecord(record)
    if not msg[0]:
        return msg
    getAddIpAddrCmd(host, ip, ttl)
    getAddPTRCmd(host, rip, ttl)
    return "success"

def getDelRecordCmd(record):
    ip = record['ip']
    rip = ('.').join(ip.split('.')[::-1]) + '.in-addr.arpa'
    ttl = 60
    host = record['domain']
    msg = checkDelRecord(record)
    if not msg[0]:
        return msg
    getDelIpAddrCmd(host, ip, ttl)
    getDelPTRCmd(host, rip, ttl)
    return "success"
    

#check add record (check ip/hostname and check dns by ip and hostname)
def checkAddRecord(record):
    if re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', record['ip']) is None:
        return ['False', 'invaild ip %s' % record['ip']]
    if re.findall(suffix, record['domain']) is None:
        return ['False', 'invaild doamin %s' % record['domain']]

    return ['True',]

#check del record
def checkDelRecord(record):
    if re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', record['ip']) is None:
        return ['False', 'invaild ip %s' % record['ip']]
    if re.findall(suffix, record['domain']) is None:
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
    if not err[0]:
        return err[1]

    result = getDelRecordCmd(record)
    return result
