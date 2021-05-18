#!/usr/bin/python3
""" API Reddit Project """
import requests


def number_of_subscribers(subreddit):
    """ Function that returns number of subs """
    page = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(page, headers={"User-Agent": "Mozilla/5.0"})
    json_req = req.json()
    if req.status_code != 200:
        return (0)
    return json_req.get('data').get('subscribers')
