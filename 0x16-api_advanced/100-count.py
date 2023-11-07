#!/usr/bin/python3
"""
queries the Reddit API and prints
top ten hot posts of a subreddit
"""
import requests
import re
import sys


def add_title(dictionary, hot_posts):
    """ Add item into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            com = re.compile("^{}$".format(key), re.I)
            if com.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ Queries Reddit API """
    params = {
	'after': after
    }
    agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': agent
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if req.status_code != 200:
        return None

    dic = req.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ fore function """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    i = sorted(dictionary.items(), key=lambda kv: kv[1])
    i.reverse()

    if len(i) != 0:
        for item in i:
            if item[1] is not 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
