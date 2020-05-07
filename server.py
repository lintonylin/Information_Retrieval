# -*- coding:utf-8 -*-
from http.server import BaseHTTPRequestHandler,HTTPServer
import json
from urllib.parse import quote
from urllib import parse
import sys
import string
import argparse
from triple import triple

parser = argparse.ArgumentParser()
parser.add_argument('--port', default=12345, help='backend port')
args = parser.parse_args()

'''
if len(sys.argv) < 2:
    print ("error! port number not input")
    exit(0)
'''

PORT_NUMBER = int(args.port)

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        p = parse.urlparse(self.path)
        qsl = parse.parse_qsl(p.query)
        content = None
        result = None
        for (para,value) in qsl:
            if para == 'content':
                content = value
        if content is not None:
            print(content)
            # result = content
            result = triple(content)
            print(result)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        if result is not None:
            self.wfile.write(json.dumps(result).encode())
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print ('Started httpserver on port ' , PORT_NUMBER)

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print ('^C received, shutting down the web server')
    server.socket.close()
