#!/usr/bin/python3
""" API Reddit Project """
import requests


def recurse(subreddit, hot_list=[]):
    """ Function that returns list of all hot posts """
    page = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    req = requests.get(page, headers={"User-Agent": "Mozilla/5.0"})
    json_req = req.json()