#!/usr/bin/python3
""" how many subs"""
import requests


def number_of_subscribers(subreddit):
    """num of suscribers"""

    headers = {
        'User-Agent': u_agent
    }

    if subreddit is None or type(subreddit) != str:
        return (0)
    url = "http://www.reddit.com/r/{}/about.json".format(
            subreddit)
    res = requests.get(url, headers=headers)
    if (res.status_code != 200):
        return (0)
    subs = res.json().get("data").get('subscribers', 0)
    return (subs)
