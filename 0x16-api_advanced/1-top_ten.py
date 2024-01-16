#!/usr/bin/python3
"""queries the Reddit API
"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit

    Args:
        subreddit: the given subreddit
    """

    headers = {"User-Agent": 'xica389'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    request = requests.get(url, headers=headers, allow_redirects=False,
                           params=params)

    if request.status_code == 200:
        titles = request.json().get("data").get("children")

        for title in titles:
            print(title.get("data").get("title"))

    else:
        print(None)
