#!/usr/bin/python3
"""
Queries the Reddit API and returns number of subscribers to a given subreddit
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """ returns number of subscribers to a given subreddit """
    headers = {'User-Agent': '113'}
    subreddit = sys.argv[1]
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"

    about = requests.get(url, headers=headers).json()
    data = about.get('data')

    return(data.get('subscribers'))
