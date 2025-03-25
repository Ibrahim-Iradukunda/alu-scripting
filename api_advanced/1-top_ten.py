#!/usr/bin/python3
"""Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Ensure valid subreddit (status_code 200)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title', '').strip())
            else:
                # Valid subreddit with no posts
                print("None")
        else:
            # Invalid subreddit or redirect
            print("None")
    except Exception:
        # Handle errors gracefully
        print("None")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Please pass an argument for the subreddit to search.")
