#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wetting my hands on functions
Exercises from https://dbwebb.se/kunskap/funktioner-argument-och-returvarden
This file is saved as a module from functions.py
"""

# functions that have a return value
def calculate_energy(timeInMicrowave, effect=800):
    """
    Calculates the energy consumption in kWh
    Returns the consumption
    """
    energy = effect * timeInMicrowave / 1000
    return energy # or return effect * timeInMicrowave/1000


def calculate_cost(energy, pricePerKWh=78.04):
    """
    Calculates the cost for a given energy consumption
    Returns the cost in kr
    """
    return energy * pricePerKWh / 100
