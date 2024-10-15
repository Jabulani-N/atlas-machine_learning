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

    list all planets
    list all sapient species
    list all planets that have somehting from sapient species list
        for specie in planet's specieses
            if in sapient species list
                say "sapient planet" and break
                    break because don't care about remaining entries on planet
    """
    pass
