#!/usr/bin/python3
"""Recurse it!"""
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """recurse the value"""
    params = {
        'after': after,
        'count': count
    }
    agent = 'Mozilla/5.0'
    headers = {'User-Agent': agent}
    url = 'http://www.reddit.com/r/{}/top/.json'.format(subreddit)
    req = requests.get(url, params=params,
                       headers=headers)
    if req.status_code >= 400:
        return None
    result = req.json().get('data')
    after = result.get('after')
    count += result.get('dist')
    res = result.get('children')
    for child in res:
        hot_list.append(child.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
