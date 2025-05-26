#!/usr/bin/env -S python3 -u

import http.server
import urllib
import sys
import json
import struct
import os
import signal
import time
import traceback
import datetime

ADDR = "127.0.0.1"
PORT = 8766
PROCESS_STARTUP_WAIT = 5

BLACKLISTED_PATHS = ["favicon.ico"]

script_path = os.path.realpath(os.path.dirname(__file__))
lockfile_path = script_path + "/.crowbar"

def error_log(message: str, error: str = "") -> None:
    try:
        utc_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
        with open(script_path + "/error.log", "a", encoding = "utf8") as log_file:
            log_file.write(utc_time + ", " + str(message).replace("\r", r"\r").replace("\n", r"\n") + ", " + str(error).replace("\r", r"\r").replace("\n", r"\n") + "\n")
    except Exception:
        # This exception cannot be "last resort" printed due to stdout being used for nativemessaging
        pass

def ensure_single_instance():
    wait_time = 0
    try:
        with open(lockfile_path, "r") as lockfile:
            os.kill(int(lockfile.read()), signal.SIGTERM)
            wait_time = PROCESS_STARTUP_WAIT
    except Exception:
        error_log(traceback.format_exc())

    with open(lockfile_path, "w") as lockfile:
        lockfile.write(str(os.getpid()))

    time.sleep(wait_time)

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

        send_message({'action': path, 'params': params})

        yomitan_response = get_message()

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(yomitan_response), "utf-8"))

try:
    ensure_single_instance()
    httpd = http.server.HTTPServer((ADDR, PORT), RequestHandler)
    httpd.serve_forever()
    delete_lockfile()
except Exception:
    error_log(traceback.format_exc())
