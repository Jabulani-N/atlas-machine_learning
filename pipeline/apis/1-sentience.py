#!/usr/bin/env python3
"""
pulls data from a paginated api
    manipulates said data
"""

import requests


def sentientPlanets():
    """
    returns names of star wars planets that meet conditions
        as accorging to SWAPI
    differs from task 0 as the conditoins have conditions
        essentially, we'll have nest

    list all sapient species
    list homeworlds of all sapient species

    trim dupes from list
    """
    planet_list = []

    # list of all sw species
    url = 'https://swapi-api.hbtn.io/api/species/'
    # get sentient species
    while url:
        response = requests.get(url)
        # data actually has the usable data dict
        data = response.json()
        # swapi has results under 'results' key
        for entry in data["results"]:
            # each entry is a species
            if entry['designation'] == "sentient":
                # swapi returns homeworld as swapi address for relevant planet
                # print(entry["name"])
                if entry["homeworld"]:
                    homeworld_response = requests.get(entry["homeworld"])
                    homeworld_data = homeworld_response.json()
                    homeworld_name = homeworld_data["name"]
                    # print("added species:", entry["name"],
                    #       "designation:",entry["designation"],
                    #       "homeworld",homeworld_name)
                    planet_list.append(homeworld_name)
        url = data['next']
    # print("survived planet scraping",)
    return planet_list
