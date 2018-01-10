#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bernard Che Longho, 2017-09-29
A file containing codes for an inventory.
Full program description and requirements are found in this link
https://dbwebb.se/uppgift/din-egen-chattbot-marvin-inventarie#krav

Program requirements:

Commands        Function
---------------------------------------------------------------------------
inv             Displays the contents of the inventory (nunmber and items).
inv pick sth*    Picks up sth and add in the inventory. Update file
inv drop sth    Deletes sth from the list. Update file.
inv drop        Empties the inventory

*sth = something(anything entered)
Contrains
    - The program does not allow for more than 4 items in the inventory

User-interaction
Program does not appear as a menu item. It scans the user's input for keywords
inv, pick or drop and then executes as required. Otherwise, program does nothing
"""

## GLOBAL VARIABLE ##
# Inventory file name
inv_file = "inv.data"

# ==========================================================================
# ==========================================================================

def open_inventory(filname):
    """
    Open the inventory file and return a string of the item(s)
    """
    with open(filname) as inv:
        line = inv.read().strip()

    return line

# ==========================================================================
# ==========================================================================

def save_inventory(ilist, filname):
    """
    Updates the inventory file with new items as picked or dropped by the user
    @ input: a list of items
             file containing items
    """
    list_size = len(ilist)
    inv_str = ",".join(ilist) if list_size > 0 else ""

    with open(filname, "w") as save_items:
        save_items.write(inv_str)

# ==========================================================================
# ==========================================================================
def showItems(ilist):
    """
    Takes a an item list and prints them out with numbers
    """
    items = len(ilist)

    word = "item" if items < 2 else "items"

    print("\tInventory has {n} {w}.".format(n=items, w=word), ilist)

# ==========================================================================
# ==========================================================================
def clear_inv_or_drop_item(ilist, ifile):
    """
    Clears the inventory is there is anything in it.
    Gives user opportunity to correct emptying the inventory
    @inparameters: inventory list(ilist)
                   inventory file(ifile)
    """
    inv_items = len(ilist)

    if inv_items > 0:
        print("\tAre you sure (Emptying the inventory)?")

        ans = input("\t(y/n)>>> ")

        if ans[0] == "Y" or ans[0] == "y":
            ilist.clear()

            save_inventory(ilist, ifile)  # save empty list
            print("\tInventary is now empty.")


        elif ans[0] == "n" or ans[0] == "N":
            item_to_drop = input("\tEnter item to drop then: ")

            if item_to_drop in ilist:
                ilist.remove(item_to_drop)
                save_inventory(ilist, ifile)  # clear file
                print("\tDropped '{itm}'".format(itm=item_to_drop))

            else:
                print("\t '%s' not in the inventory." %item_to_drop)

        else:
            print("\t'%s' is invalid choice." %ans)

    else:
        print("\tThe inventory is already empty. Nothing to drop.")

# ==========================================================================
# ==========================================================================

def pick_item(ilist, ifile, item, maxItems):
    """
    Takes an item picked and save to file
    @inparameters: inventory list (ilist)
                   inventory file(ifile)
                   maximum number of items allowed(maxItems)
                   item to save to file (item)
    """
    inv_items = len(ilist)
    max_list = maxItems

    if inv_items < max_list:
        print("\tYou picked '{itm}'".format(itm=item))
        ilist.append(item)
        save_inventory(ilist, ifile)
    else:
        print("\tMaximum picks(%s) reached!" %inv_items)

# ==========================================================================
# ==========================================================================

def drop_item(ilist, ifile, item):
    """
    If item entered is in the list, it is dropped.
    When dropped, file is updated
    If item is not found in the list, user is informed and no drop is done
    """
    if item in ilist:
        ilist.remove(item)
        save_inventory(ilist, ifile)
        print("\tYou dropped '{itm}'".format(itm=item))
    else:
        print("\t'{itm}' is not in inventory.".format(itm=item))

# ==========================================================================
# ==========================================================================

def invalid_command(command, valid_commands):
    """
    Checks if a command is not part of the inventory menu commands
    """
    print("\t'{ch}' is not recognized in inventory menu".format(ch=command))
    print("\tUse", valid_commands, "eg {c1} {c2} ".format(c1=valid_commands[0], c2=valid_commands[1]))

# ==========================================================================
# ==========================================================================

def manage_inventory(choice):
    """
    Make an inventory that permits the user to pick, drop or clear the content
    of the inventory
    """
    max_list = 4
    inv_menu = ["inv", "pick", "drop"]

    line = open_inventory(inv_file)

    line_size = len(line)

    inv_list = line.split(",") if line_size > 0 else list()

    command = choice.lower().split()  # convert user input and split the words

    commands = len(command)

    # user entered just one string
    if commands == 1:
        if command[0] == inv_menu[0]:
            showItems(inv_list)

    # user entered two strings
    elif commands == 2 and command[0] == inv_menu[0]:
        if command[1] == inv_menu[1]:
            print("\tYou attempted picking something. I didn't get it.")
            print("\tUsage: inv pick <something>")

        elif command[1] == inv_menu[2]:
            clear_inv_or_drop_item(inv_list, inv_file)

        elif command[1] not in inv_menu:
            invalid_command(command[1], inv_menu)

# user inputs three words
    elif commands >= 3 and command[0] == inv_menu[0]:
        if command[1] == inv_menu[1]:
            pick_item(inv_list, inv_file, " ".join(command[2:]), max_list)

        elif command[1] == inv_menu[2]:
            drop_item(inv_list, inv_file, command[2])
        elif command[1] not in inv_menu:
            invalid_command(command[1], inv_menu)

# =============================================================================
# Test the program here
# choice = "inv"
# manage_inventory(choice)
