#!/usr/bin/env python
# coding=utf-8


import os, sys
import dns.resolver
import dns.query
import dns.update

update = dns.update.Update('xiaojukeji.com')

update.delete('test')

repsonse1= dns.query.tcp(update, '172.16.3.131')

print repsonse1
