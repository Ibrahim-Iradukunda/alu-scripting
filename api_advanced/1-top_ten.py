#!/usr/bin/python3
"""Contains top_ten function"""
import requests



def top_ten(subreddit):
    """Print the titles of the 10 hottest."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 404:
            print("None")
            return
        results = response.json().get("data")
        if results:
            [print(c.get("data").get("title")) for c in results.get("children")]
        else:
            print("None")
    except requests.RequestException:
        print("None")
    except ValueError:
        print("None")
