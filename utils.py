#!/usr/bin/env python
# coding=utf-8


import os
import sys
import re
import socket
import commands
from config import suffix
server = '172.16.3.131'

#get dns (support by ip and hostname)
def getDns(record):
    #判断是IP or hostname

    if record is ip:
        try:
            socket.gethostbyaddr(record)
            return True
        except socket.herror,e:
            return False 
    else:
        try:
            socket.getaddrinfo(record, None)
            return True
        except socket.gaierror, e:
            return False

#get ip by hostname
def getIpByHost(ip):
    
    try:
        result = socket.gethostbyaddr(ip)
        return "sucess to get hostname by ip: %s hostname: %s" % (ip, result[0])
    except socket.herror, e:
        return "faled to get hostname by ip: %s" % ip 

#get hostname by ip
def getHostByIp(hostname):
    try:
        result = socket.getaddrinfo(hostname, None)
        return "sucess to get ip by hostname: %s ip: %s" % (hostname, result[0][4])
    except socket.gaierror, e:
        return "faled to get ip by hostname: %s" % hostname 

#get dns by ip and check by hostname(ip<-->hostname，return True)
def getDnsIp(ip, hostname):
    ip_host = getIpByHost(ip)
    host_ip = getHostByIp(hostname)
    
    if ip_host is not  hostname and host_ip is not  ip:
        return "please check ip or hostname"

def getAddIpAddrCmd(host, ip, ttl):
    cmd = "echo $'server %s \nupdate add %s %d A %s\r\nsend \r\nquit\n' | nsupdate -t5 -v -k ./nsupdate.key -v" % (server, host, ttl, ip)
    result = commands.getstatusoutput(cmd)
    return result

def getAddPTRCmd(host, rip, ttl):
    cmd = "echo $'server %s \nupdate add %s %d PTR  %s\r\nsend \r\nquit\n' | nsupdate -t5 -v -k ./nsupdate.key -v" % (server, rip, ttl, host)
    result = commands.getstatusoutput(cmd)
    return result

def getDelIpAddrCmd(host, ip, ttl):
    cmd = "echo $'server %s \nupdate delete %s %d A %s\r\nsend \r\nquit\n' | nsupdate -t5 -v -k ./nsupdate.key -v" % (server, host, ttl, ip)
    result = commands.getstatusoutput(cmd)
    return result

def getDelPTRCmd(host, rip, ttl):
    cmd = "echo $'server %s \nupdate delete %s %d PTR %s\r\nsend \r\nquit\n' | nsupdate -t5 -v -k ./nsupdate.key -v" % (server, rip, ttl, host)
    result = commands.getstatusoutput(cmd)
    return result

def getAddRecordCmd(record):
    ip = record['ip']
    rip = ('.').join(ip.split('.')[::-1]) + '.in-addr.arpa'
    ttl = 60
    host = record['domain']
    msg = checkAddRecord(record)
    if not msg[0]:
        return msg
    aresult = getAddIpAddrCmd(host, ip, ttl)
    if aresult[0]:
        return ("fail", aresult[1])
    presult = getAddPTRCmd(host, rip, ttl)
    if presult[0]:
        return ("fail", presult[1])
    return ("sucess", " ")

def getDelRecordCmd(record):
    ip = record['ip']
    rip = ('.').join(ip.split('.')[::-1]) + '.in-addr.arpa'
    ttl = 60
    host = record['domain']
    msg = checkDelRecord(record)
    if not msg[0]:
        return msg
    aresult = getDelIpAddrCmd(host, ip, ttl)
    if aresult[0]:
        return ("fail", aresult[1])
    presult = getDelPTRCmd(host, rip, ttl)
    if presult[0]:
        return ("fail", presult[1])
    return ("sucess", " ")
    

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
