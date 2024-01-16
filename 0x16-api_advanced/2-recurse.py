#!/usr/bin/python3
"""queries the Reddit API
"""

import requests

after = None


def recurse(subreddit, hot_list=[]):
    """

    Args:
        subreddit: the given subreddit
        hot_list: list of hot titles in the given subreddit

    Returns:
        returns a list containing the titles of all hot articles for a given
        subreddit
    """

    global after

    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    request = requests.get(url, headers=headers, allow_redirects=False,
                           params=params)

    if request.status_code == 200:
        next = request.json().get('data').get('after')

        if next is not None:
            after = next
            recurse(subreddit, hot_list)

        titles = request.json().get('data').get('children')

        for title in titles:
            hot_list.append(title.get('data').get('title'))

        return hot_list

    else:
        return (None)
