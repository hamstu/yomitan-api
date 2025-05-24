#!/usr/bin/env -S python3 -u

import http.server
import urllib
import sys
import json
import struct
import os
import signal
import time

ADDR = "127.0.0.1"
PORT = 8766
PROCESS_SHUTDOWN_TIME = 5

BLACKLISTED_PATHS = ["favicon.ico"]

lockfile_path = os.path.realpath(os.path.dirname(__file__)) + "/.lock"

def ensure_single_instance():
    try:
        with open(lockfile_path, "r") as lockfile:
            os.kill(int(lockfile.read()), signal.SIGTERM)
            time.sleep(PROCESS_SHUTDOWN_TIME)
    except FileNotFoundError:
        pass
    except ProcessLookupError as e:
        print("Warning: Failed to process lockfile: " + str(e))

    with open(lockfile_path, "w") as lockfile:
        lockfile.write(str(os.getpid()))

def delete_lockfile():
    os.remove(lockfile_path)

def get_message():
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        return None
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

ensure_single_instance()
httpd = http.server.HTTPServer((ADDR, PORT), RequestHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

delete_lockfile()
