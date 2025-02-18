#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define custom User-Agent to avoid rate limiting issues
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    
    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception as e:
        return 0

