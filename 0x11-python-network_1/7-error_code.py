#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
handling error appropriately
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
