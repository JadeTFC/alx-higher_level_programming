#!/usr/bin/python3
""" Fetch 10 commits in reverse chronological order """
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    params = {"per_page": 10}
    r = requests.get(url, params=params)
    commits = r.json()
    for commit in commits:
        print("{}: {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name"))
        )
