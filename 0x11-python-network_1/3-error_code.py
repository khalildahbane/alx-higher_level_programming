#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as resp:
            body = resp.read()
            print(body.decode())
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
