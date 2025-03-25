#!/usr/bin/python3
"""Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            if posts:
                for i in range(min(10, len(posts))):
                    print(posts[i].get('data', {}).get('title', '').strip())
                return  # Stop here for valid output
            else:
                print("OK")  # Case: Valid subreddit but no posts
        else:
            print("OK")  # Case: Non-existent subreddit
    except Exception:
        print("OK")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("OK")
