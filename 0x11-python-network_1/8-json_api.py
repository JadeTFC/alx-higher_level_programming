#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}

    r = requests.post("http://0.0.0.0:5000/search_user", data)

    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
