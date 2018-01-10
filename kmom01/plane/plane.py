#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lobe16 (blongho)
2017-09-01
Program to convert speed, temperature and height in diferent units
"""
from datetime import datetime
#print("Hej Jack Black, du är 48 år gammal.")

i = datetime.now()
current_year = i.year
print("Today's date(dd-mm-yyyy): %d-%d-%d\nTime: %d:%d:%d" %(i.day, i.month, i.year, i.hour, i.minute, i.second))
name = input("\nSkriv ett namn, klicka sen enter : ")
age = input("\nSkriv en ålder, klicka sen enter : ")

year_born = str(current_year - int(age))
greeting = "\nHej " + name + ", du är " + str(age) + " år gammal och föddes år "\
            + year_born
print(greeting)

heightInMeter = input("\nMäta in planens höjden över havet [meter] : ")

speedInKmHr = input("\nMäta in planens hastigheten [km/h] : ")

celciusTemp = input("\nMäta in temperaturen utanför planen [°C] : ")

meterToFeet = 3.28084

kilometerToMiles = 0.62137

heightInFeet = float(heightInMeter) * meterToFeet

speedInMilesHr = float(speedInKmHr) * kilometerToMiles

fahTemp = (float(celciusTemp) * 9 / 5) + 32

print("\n========================================================"\
"\nHöjd över havet =  " + str(round(heightInFeet, 2)) + " ft." +\
"\n\nHastigheten = " + str(round(speedInMilesHr, 2)) + " mph." +\
"\n\nTemperaturen utanför planen = " + str(round(fahTemp, 2)) + " °F."\
"\n========================================================")
