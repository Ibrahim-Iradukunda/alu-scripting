#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    try:
        response = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                                .format(subreddit), headers=user)
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        for post in data.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print(None)
