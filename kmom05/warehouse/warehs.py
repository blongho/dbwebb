#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
2017-10-04
Bernard Che Longho
Working with dictionaries and tuples in python as per exercises in
https://dbwebb.se/kunskap/dictionaries-och-tupler-i-python
"""
warehouse = {
    "köttfärs" : 20,
    "grädde" : 80,
    "krossade tomater" : 33,
    "gul lök" : 42
}

print(warehouse)
#print(warehouse["krossade tomater"])

# modifying contents in the warehouse
warehouse["krossade tomater"] = 58
warehouse["gul lök"] = 7

print(warehouse)

# Loop through dictionary key-values using items()
for key, value in warehouse.items():
    print(key.ljust(17), str(value).rjust(3))

# using the sorted() and keys() methods to sort a dictionary
for key in sorted(warehouse.keys()):
    print(str(key).ljust(17), str(warehouse[key]).rjust(3))

"""
A dictionaryy of dictionaries
"""
warehouse_deluxe = {
    "köttfärs" : {"stock" : 20, "price" : 50},
    "grädde" : {"stock" : 80, "price" : 20},
    "krossade tomater" : {"stock" : 33, "price" : 10},
    "gul lök" : {"stock" : 42, "price" : 5}
    }

# show warehouse_deluxe
print(warehouse_deluxe)

# print items sorted by keys showing the prices
for key in sorted(warehouse_deluxe.keys()):
    print(key, warehouse_deluxe[key]["price"])

"""
tuples
"""
warehouse_deluxe2 = {
    "köttfärs" : {"stock" : 20, "price" : 50, "ids" : (1234, "K14")},
    "grädde" : {"stock" : 80, "price" : 20, "ids" : (3141, "L12")},
    "krossade tomater" : {"stock" : 33, "price" : 10, "ids" : (4224, "E13")},
    "gul lök" : {"stock" : 42, "price" : 5, "ids" : (2742, "D02")}
    }

print(warehouse_deluxe2)

warehouse_deluxe2["röd lök"] = {}
print(warehouse_deluxe2)
warehouse_deluxe2["röd lök"]["stock"] = 7
print(warehouse_deluxe2)
warehouse_deluxe2["röd lök"]["price"] = 9
print(warehouse_deluxe2)
warehouse_deluxe2["röd lök"]["ids"] = (6314, "D04")
print(warehouse_deluxe2)
