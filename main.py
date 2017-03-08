#!/usr/bin/env python
# coding=utf-8

import sys
import logging
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass = BaseHTTPServer.HTTPServer
Protocol = 'HTTP/1.0'

#log日志初始化
def initlog():
    pass


#绑定监听端口
def listenServer():
    pass

#
def main():
    ...

    initlog()
    listenServer()

if __name__ == '__main__':
    main()



