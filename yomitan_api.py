#!/usr/bin/env -S python3 -u

import http.server
import urllib
import sys
import json
import struct

ADDR = "localhost"
PORT = 8766

BLACKLISTED_PATHS = ["favicon.ico"]

def get_message():
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        return {'action': None}
    message_length = struct.unpack('@I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode('utf-8')
    return json.loads(message)

def send_message(message_content):
    encoded_content = json.dumps(message_content).encode('utf-8')
    encoded_length = struct.pack('@I', len(encoded_content))
    sys.stdout.buffer.write(encoded_length)
    sys.stdout.buffer.write(encoded_content)
    sys.stdout.buffer.flush()

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path[1:]
        params = urllib.parse.parse_qs(parsed_url.query)

        if path in BLACKLISTED_PATHS:
            self.send_response(400)
            self.end_headers()
            return

        send_message({'action': path, 'params': params, 'sequence': 1})

        yomitan_response = get_message()

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(yomitan_response), "utf-8"))

httpd = http.server.HTTPServer((ADDR, PORT), RequestHandler)
httpd.serve_forever()
