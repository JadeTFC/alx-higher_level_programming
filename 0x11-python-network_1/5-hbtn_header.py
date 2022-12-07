#!/usr/bin/python3
""" Takes a URL and retrieve the header value of the X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
