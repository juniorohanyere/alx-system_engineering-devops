#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API

    Args:
        subreddit: subreddit name

    Return:
        returns the number of subscribers
    """

    headers = {"User-Agent": "Custom"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")

    return 0
