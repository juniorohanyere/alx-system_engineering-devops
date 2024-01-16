#!/usr/bin/python3
"""queries the Reddit API
"""

import requests

after = None
count = []


def count_words(subreddit, word_list):
    """parses the title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces)
    """

    global after
    global count

    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    request = requests.get(url, headers=headers, allow_redirects=False,
                           params=params)
