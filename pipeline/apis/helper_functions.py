#!/usr/bin/env python3
"""
helper functions to streamline other modules
"""

import requests


def api_paginator(url, subject_key=None, next_page_key="Next",
                  max_pages=None,
                  ):
    """
    INCOMPLETE

    when finished, can be used to create an unconditoinal list
    that can be curated via another api call

    recieves api url and subject key we want all entries from
        expects a dicitonary from the api call
    returns a list of all entries of subject_key from the api's dictoinary
    """
    data_list = []
    while url:
        response = requests.get(url)
        # data actually has the usable data dict
        data = response.json()
        if subject_key:
            for entry in data[subject_key]:
                if entry[subject_key]:
                    data_list.append(entry[subject_key])
            # this will move the url to the next page
            #   until None is next
            if data[next_page_key]:
                url = data[next_page_key]
            else:
                url = None
        else:
            # if we just want the whole dictionary
            for entry in data:
                if entry:
                    data_list.append(entry)
            # this will move the url to the next page
            #   until None is next
            if data[next_page_key]:
                url = data[next_page_key]
            else:
                url = None
    return data_list
