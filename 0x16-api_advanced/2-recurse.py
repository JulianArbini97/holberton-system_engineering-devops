#!/usr/bin/python3
""" API Reddit Project """
import requests


def recurse(subreddit, hot_list=[], next_page=''):
    """ Function that returns list of all hot posts """
    page = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, next_page)
    req = requests.get(page, headers={"User-Agent": "Mozilla/5.0"})
    json_req = req.json()
    posts = json_req.get('data').get('children')
    if req.status_code != 200:
        return None
    else:
        for title in posts:
            hot_list.append(title.get('data').get('title'))
        next_page = json_req.get('data').get('after')
        if next_page:
            recurse(subreddit, hot_list, next_page)
        return hot_list
    return hot_list
