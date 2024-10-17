#!/usr/bin/env python3
"""
script, not run when imported
uses GitHub api

pulls data from a rate limited api
    manipulates said data
"""

import requests
import sys
import time


def get_location(user_url=None):
    """
    github api

    gets location of user specified
        user_url
    """
    response = requests.get(user_url)
    status_code = response.status_code
    data = response.json()
    if status_code == 403:
        # Forbidden
        #   likely rate limit reached
        # print("Exodia the forbidden route")
        unix_reset_time = response.headers.get('X-RateLimit-Reset',
                                               0)
        unix_reset_time = int(unix_reset_time)
        unix_current_time = int(time.time())
        # these times are in seconds
        seconds_reset_time = unix_reset_time - unix_current_time
        minutes_reset_time = seconds_reset_time / 60
    elif status_code == 200:
        # get the user's location
        # print("success route")
        print(data.get("location", "Location not provided"))
    elif status_code == 404:
        print("Not found")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # first argument is script call itself
        user_url = sys.argv[1]
        get_location(user_url)
    else:
        # do the action you do when oyu get no url
        pass
