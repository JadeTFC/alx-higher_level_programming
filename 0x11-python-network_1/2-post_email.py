#!/usr/bin/python3
""" sends a POST request to the passed URL """
from urllib import request, parse
import sys

if __name__ == "__main__":
    values = {"email": sys.argv[2]}
    data = parse.urlencode(values).encode("ascii")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf8"))
