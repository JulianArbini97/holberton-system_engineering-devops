#!/usr/bin/python3
""" API Reddit Project """
import requests


def top_ten(subreddit):
    """ Function that returns last 10 posts """
    page = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    req = requests.get(page, headers={"User-Agent": "Mozilla/5.0"})
    json_req = req.json()
    if req.status_code != 200:
        print("None")
    else:
        posts = json_req.get('data').get('children')
        for title in posts:
            print(title.get('data').get('title'))
