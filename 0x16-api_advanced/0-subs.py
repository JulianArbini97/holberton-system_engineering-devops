#!/usr/bin/python3
""" API Reddit Project """
import requests


def number_of_subscribers(subreddit):
    """ Function that returns number of subs """
    page = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(page)
    json_req = req.json()
    if json_req.get('error') == 404:
        return (0)
    return json_req.get('data').get('subscribers')
