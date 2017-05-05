#!/usr/bin/env python
#coding: utf8
#for python 2.7

import zmq
import sys, os

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)
context = zmq.Context()
print("Connecting to server...{0}".format(os.linesep))
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

#  Do 10 requests, waiting each time for a response
for request in range (1,10):
    print("Sending request {0} ...".format(request))
    socket.send ("Hello")
    #  Get the reply.
    message = socket.recv()
    print("Received reply {0}[{1}]".format(request, message))
    

