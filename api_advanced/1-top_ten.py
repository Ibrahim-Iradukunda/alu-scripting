#!/usr/bin/python3
"""Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}

    # Make the request and prevent redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for non-200 status codes (e.g., invalid subreddit)
    if response.status_code != 200:
        print(None)
        return

    # Extract posts data
    posts = response.json().get('data', {}).get('children', [])
    if not posts:
        # Handle case where subreddit exists but has no posts
        print(None)
        return

    # Print the titles of the top 10 hot posts
    for i in range(min(10, len(posts))):
        print(posts[i].get('data', {}).get('title', '').strip())
