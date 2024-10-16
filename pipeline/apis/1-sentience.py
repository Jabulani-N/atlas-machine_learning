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
    list all planets that have somehting from sapient species list
        for specie in planet's specieses
            if in sapient species list
                say "sapient planet" and break
                    break because don't care about remaining entries on planet

    ideally, we'd limit api call count
        but first make it work at all
    """
    sent_spec_list = []
    planet_list = []

    # list of all sw species
    url = 'https://swapi-api.hbtn.io/api/species/'
    relevant_names = []
    # get sentient species
    while url:
        response = requests.get(url)
        # data actually has the usable data dict
        data = response.json()
        # swapi has results under 'results' key
        for entry in data["results"]:
            if entry['designation'] == "sentient":
                sent_spec_list.append(entry["name"])
        url = data['next']

    return relevant_names
