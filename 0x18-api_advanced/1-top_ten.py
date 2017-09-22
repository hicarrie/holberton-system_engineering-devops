#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit
"""

import requests
import sys


def top_ten(subreddit):
    """ returns titles of the first 10 hot posts for a given subreddit """
    headers = {'User-Agent': '113'}
    subreddit = sys.argv[1]
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"

    about = requests.get(url, headers=headers)
    if not about:
        print("None")
    else:
        data = about.json().get('data').get('children')
        if not data:
            print("None")
        for post in data:
            print(post.get('data').get('title'))
