#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the
response handling error appropriately
"""
from urllib import request, error as urlerror
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf8"))
    except urlerror.HTTPError as e:
        print("Error code: {}".format(e.code))
