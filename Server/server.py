from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import socket

address = ('localhost', 8081)

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('path = {}'.format(self.path))

        parsed_path = urlparse(self.path)
        print('parsed: path = {}, query = {}'.format(parsed_path.path, parse_qs(parsed_path.query)))

        print('headers\r\n-----\r\n{}-----'.format(self.headers))

        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        if parsed_path.path == "/hi":
            
            self.send_response(200)
            self.send_header('Hello','BasicHTTP!')
            self.send_header('Content-Lengt','13')
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            address = ip.encode()
            self.wfile.write(address)
        else:
            self.send_header('Not page','Prease retry HTTP.')
            self.end_headers()
        

    def do_POST(self):
        print('path = {}'.format(self.path))

        parsed_path = urlparse(self.path)
        print('parsed: path = {}, query = {}'.format(parsed_path.path, parse_qs(parsed_path.query)))

        print('headers\r\n-----\r\n{}-----'.format(self.headers))

        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        content_length = int(self.headers['content-length'])
        
        print('body = {}'.format(self.rfile.read(content_length).decode('utf-8')))
        
        self.send_response(200)
        self.send_header('Hello','BasicHTTP!')
        self.send_header('Content-Lengt','13')
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

        #self.wfile.write(ip)

with HTTPServer(address, MyHTTPRequestHandler) as server:
    server.serve_forever()
