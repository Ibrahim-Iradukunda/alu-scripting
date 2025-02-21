#!/usr/bin/python3
"""
1-top_ten module
"""
import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            for post in data:
                print(post.get("data", {}).get("title", "None"))
        else:
            print(None)
    except requests.RequestException:
        print(None)
