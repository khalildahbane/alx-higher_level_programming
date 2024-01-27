#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    api_git = "https://api.github.com/user"
    req = requests.get(api_git, auth=(sys.argv[1], sys.argv[2]))
    r = req.json()
    print(r.get("id"))
