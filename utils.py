#!/usr/bin/env python
# coding=utf-8


import os
import sys


#reverse the ip and return
def reverseIP(s):
    pass

#get dns (support by ip and hostname)
def getDns(s):
    pass

#get ip by hostname
def getIpByHost(hostname)
    pass

#get hostname by ip
def getHostByIp(ip):
    pass

#get dns by ip and check by hostname(ip<-->hostname，return True)
def getDnsIp(ip , hostname):
    pass

#执行command
def  runcmd(command):
    pass

def getAddIpAddrCmd(hostname, ip):
    pass

def getAddPTRCmd(reversedIp, hostname):
    pass

def getDelPTRCmd(reversedIp, hostname):
    pass

def getAddRecordCmd(r):
    pass

def getDelRecordCmd(r):
    pass

#check add record (check ip/hostname and check dns by ip and hostname)
def checkAddRecord(r):
    pass

#check del record
def checkDelRecord(r):
    pass

#check mod record
def checkModRecord(r):
    pass

#add the record (by check and add)
def addRecord(r):
    pass

#del the record (by check and del)
def delRecord(r):
    pass

#mod the record (by check, del and add)
def modRecord(r):
    pass

def removeDupRecords(records):
    pass
