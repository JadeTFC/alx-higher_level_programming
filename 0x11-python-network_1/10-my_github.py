#!/usr/bin/python3
""" Use Github API to display id """
import requests
import sys

if __name__ == "__main__":
    GITHUB_API = "https://api.github.com/user"
    auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(GITHUB_API, auth=auth)

    if r.status_code >= 400:
        print(None)
    else:
        try:
            json = r.json()
            print(json.get("id"))
        except Exception:
            print(None)
