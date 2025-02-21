#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # Check if the request was successful
        if RESPONSE.status_code != 200:
            print("None")
            return

        DATA = RESPONSE.json().get("data")

        # Check if 'data' exists and has 'children'
        if not DATA or "children" not in DATA:
            print("None")
            return

        HOT_POSTS = DATA["children"]

        # Print the top 10 post titles
        for post in HOT_POSTS:
            print(post["data"].get("title", "None"))

    except Exception:
        print("None")

