#!/usr/bin/python3
"""top ten api"""
import requests


def top_ten(subreddit):
    """list top 10 reddit api"""
    agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': agent
    }

    params = {
        'limit': 10
    }

    if subreddit is None or type(subreddit) != str:
        print('None')
        return
    url = "http://www.reddit.com/r/{}/top/.json".format(subreddit)
    req = requests.get(url, params=params,
                       headers=headers)
    if req.status_code != 200:
        print('None')
        return
    res = req.json().get('data').get('children')
    for child in res:
        title = child.get('data').get('title')
        print(title.encode('utf-8'))
