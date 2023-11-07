#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles of
all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests
others = None


def recurse(subreddit, hot_list=[]):
    """ returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given subreddit,
    the function should return None."""
    global others
    headers = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': others}
    results = requests.get(url, params=parameters, headers=headers,
                           allow_redirects=False)
    if results.status_code == 200:
        next_items = results.json().get("data").get("after")
        if next_items:
            others = next_items
            recurse(subreddit, hot_list)
        titles = results.json().get("data").get("children")
        for title in titles:
            hot_list.append(title.get("data").get("title"))
        return hot_list
    else:
        return (None)
