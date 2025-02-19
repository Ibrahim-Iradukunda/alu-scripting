#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    # Set up the API endpoint and headers
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:alu-scripting:v1.0.0 (by /u/your_username)"
    }

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        # Print the titles of the first 10 hot posts
        for i in range(min(10, len(posts))):
            print(posts[i]["data"]["title"])
    else:
        print(None)


if __name__ == '__main__':
    top_ten("programming")
