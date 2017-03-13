#!/usr/bin/env python
# coding=utf-8

import simplejson as json
import logging

FIELD = ['listen', 'tokens', 'ips', 'logdir', 'asuffix', 'psuffix']


with open('config.json', 'r')  as f:
    config =  json.load(f)
    listen = config['listen']
    tokens = config['tokens']
    ips = config['ips']
    asuffix = config['asuffix']
    psuffix = config['psuffix']
    logdir = config['logdir']

def parserConfig(cfg):
    pass


def updateConfig(cf):
    pass
