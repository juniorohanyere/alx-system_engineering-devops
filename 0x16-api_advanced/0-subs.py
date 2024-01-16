#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers
'''

import requests
import sys


def number_of_subscribers(subreddit):
    '''queries the Reddit API

    Args:
        subreddit: subreddit name

    Return:
        returns the number of subscribers
    '''

    headers = {"User-Agent": "xica369"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    return response.json().get("data").get("subscribers") if \
        response.status_code == 200 else 0
