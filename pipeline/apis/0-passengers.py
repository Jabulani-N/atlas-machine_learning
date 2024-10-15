#!/usr/bin/env python3
"""
pulls data from a paginated api
    manipulates said data
"""

import requests


def availableShips(passengerCount=None):
    """
    returns names of star wars vehicles that meet conditions
        as accorging to SWAPI
    """
    url = 'https://swapi.dev/api/starships/'
    relevant_names = []
    # entrynum = 0
    while url:
        response = requests.get(url)
        # this part actually has the usable data dict
        data = response.json()
        # print("response number ",entrynum, ": ",response)
        # print("data number ",entrynum, ": ",data)
        # entrynum += 1

        for entry in data["results"]:
            if entry["passengers"] != "n/a" and\
                    entry["passengers"] != "unknown":
                # size matters
                if int(entry["passengers"].replace(",", "")) >= passengerCount:
                    relevant_names.append(entry["name"])
        # swapi gives reponse data in the form of pages
        # this will move the url to the next page
        #   until None is next
        url = data['next']
    return relevant_names
