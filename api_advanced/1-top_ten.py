#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # Check if the response is valid
        if RESPONSE.status_code != 200:
            print("None")
            return
        
        DATA = RESPONSE.json().get("data")
        if not DATA:
            print("None")
            return
        
        HOT_POSTS = DATA.get("children", [])
        
        if not HOT_POSTS:
            print("None")
            return
        
        for post in HOT_POSTS:
            print(post.get('data', {}).get('title', "None"))

    except Exception as e:
        print("None")
