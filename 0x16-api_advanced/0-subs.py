#!/usr/bin/python3
"""
get number of subs in a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = get(url, headers=headers)
    results = response.json()

    try:
        return results.get('data').get('subscribers')
    except Exception:
        return 0
