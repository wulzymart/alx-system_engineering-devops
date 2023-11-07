#!/usr/bin/python3
"""
Module containing function that
prints the titles of the first 10 hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """

    if not subreddit or not isinstance(subreddit, str):
        print("None")

    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    response = get(url, headers=headers, params=params)
    results = response.json()

    try:
        posts = results.get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    except Exception:
        print("None")
