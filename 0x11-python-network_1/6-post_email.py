#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
import requests
import sys

if __name__ == "__main__":
    response = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(response.text)
