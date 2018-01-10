#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wetting my hands on functions
Exercises from https://dbwebb.se/kunskap/funktioner-argument-och-returvarden
"""
"""
Problem:
Två kollegor ska äta lunch tillsammans och har båda med lunchlådor.
Dansken Emil har med Rød Pølse och Svensken Andreas har med köttbullar med
mos. Emil värmer sin mat i microvågsugnen på 800W i 2,5 minuter och Andreas
värmer också sin mat på 800W, men i 3,5 minuter. Hur mycket energi går det
åt till att värma varje maträtt? Vad kostar det att värma maten med ett kWh
pris på 78.04 öre per kWh?

From the above, we have that
    Emil warms his food for 2.5 minutes at 800W
    Andreas warms his food for 3.5 minutes at 800W
    kWh price for electricity is 78.04 öre per kWh

    energy = effect * time / 1000
"""
emil_time = 2.5 / 60
andreas_time = 3.5 / 60

emil_energy = 800 * emil_time / 1000
andreas_energy = 800 * andreas_time / 1000

print("Emil uses", round(emil_energy, 4), "kWh")
print("Andreas uses", round(andreas_energy, 4), "kWh")

price_per_kWh = 78.04

emil_cost = emil_energy * price_per_kWh / 100
andreas_cost = andreas_energy * price_per_kWh / 100

print("Emil's lunch costs", round(emil_cost, 4), "kr")
print("Andreas's lunch costs", round(andreas_cost, 4), "kr")
#
# def calculate_energy():
#     """
#     Calculates the energy concumption in kWh
#     """
#     emil_energy = 800 * emil_time / 1000
#     print("Emil uses", round(emil_energy, 4), "kWh")
#
# def calculate_energy(time_in_microwave, name):
#     """
#     Calculates the energy consumption i kWh
#     And prints the consumption together with the name
#     """
#     energy = 800 * time_in_microwave / 1000
#     print(name, "uses", round(energy, 4), "kWh")
#
# print("\nPrinting from functions.")
# calculate_energy(emil_time, "Emil")
# calculate_energy(andreas_time, "Andreas")
#
# re-writing the energy calculator to take one more variable
# def calculate_energy(timeInMicrowave, name, effect=800):
#     """
#     Calculates the energy consumption in kWh
#     And prints the consumption 2gether with the name
#     The predefined value for effect is replaced by any value
#     specified when the function is called
#     """
#     energy = effect * timeInMicrowave / 1000
#     print(name, "uses", round(energy, 4), "kWh")

# using our new funtion with three arguments
kenneth_and_michael_time = 0.5 / 60

print("\nNow printing from the function that has three arguments.")
calculate_energy(kenneth_and_michael_time, "Michael", 600)
calculate_energy(kenneth_and_michael_time, "Kenneth", 800)
calculate_energy(emil_time, "Emil", 700)

# cals the function with two variables
print("\nNow calling the function that has two arguments. ")
calculate_energy(emil_time, "Emil")
calculate_energy(andreas_time, "Andrease")

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

# calling the functions with return values.
# Python auto-detects which function to call

emil_energy = calculate_energy(emil_time)

emil_cost = calculate_cost(emil_energy)

# show our new results
print("\nPrinting new calculated values...")
print("Emil uses", round(emil_energy, 4), "kWh and this costs", round(
    emil_cost, 4), "kr.")

# string formatting with .format
niceString = "Emil users {energy} kWh and this costs {cost} kr".format(
    energy=emil_energy, cost=emil_cost)

print("\nThe formated string is: ", niceString)
