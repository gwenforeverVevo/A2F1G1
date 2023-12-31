import sys
import os
from Ticket import *
from Bill import *
import datetime


def mainMenu():
    # generates the main menu information and stores the data in a dictionary,
    # return the menu dictionary
    # clear the contents of the bill.txt file whenever a new user uses this system.
    open('bill.txt', 'w').close()
    menuDictionary = {"1": "Add ticket", "2": "Buy ticket",
                      "3": "Show Records", "4": "Quit"}
    # os.system('4')
    print("*****BTS Concert*****\n")
    while (True):

        print("\nFunction menu:")

        for key, value in menuDictionary.items():
            print(f"{key}. {value}")

        inputMenu = (input("\nEnter selection (1-4): "))
        match inputMenu:
            case "1":
                addNewTicket()
                # Clearing the Screen

            case "2":
                buyTicket()
                # Clearing the Screen

            case "3":
                showRecords()
                # Clearing the Screen

            case "4":
                print('\nThank you for using the system.\n')
                sys.exit()
            case "6":
                # Error handling
                ticketMenuTestCheck()
            case _:
                print("\nError, Input the correct Value!")


def ticketMenu():
    # – generate available ticket type for selection by reading the data from ticket.txt
    # file and store the data into a dictionary. Return the dictionary
    ticketMenuDictionary = {}
    with open('Ticket.txt', 'r') as f:
        for line in f:
            ticketDetails = line.strip().split(',')
            ticketZone = ticketDetails[0]
            zoneCapacity = ticketDetails[1]
            ticketPrice = ticketDetails[2]
            ticketMenuDictionary[line] = Ticket(
                ticketZone, zoneCapacity, ticketPrice)
    return ticketMenuDictionary


def addNewTicket():
    ticketDictionary = {}
    # os.system('cls')
    while True:
        ticketZone = input("Enter ticket zone (or 'q' to quit): ")
        if ticketZone.lower() == "q":
            print("Adding Ticket process has been canceled :)")
            break
        
        if ticketZone in ticketDictionary:
            print("Ticket zone already exists. Please enter a different zone.")
            continue
        
        # Check if the ticket zone already exists in the file
        with open("Ticket.txt", "r") as file:
            for line in file:
                existingZone = line.strip().split(",")[0]
                if existingZone == ticketZone:
                    print("Ticket zone already exists. Please enter a different zone.")
                    break
            else:
                # Zone does not exist, proceed with adding the ticket
                zoneCapacity = input("Enter zone capacity: ")
                if not zoneCapacity.isdigit() or int(zoneCapacity) <= 0:
                    print("Invalid input. Capacity must be a positive integer.")
                    input("Press Enter to retry...")
                    continue
                zoneCapacity = int(zoneCapacity)

                ticketPrice = input("Enter price: ")
                if not ticketPrice.replace('.', '', 1).isdigit() or float(ticketPrice) <= 0:
                    print("Invalid input. Price must be a positive numeric value.")
                    input("Press Enter to retry...")
                    continue
                ticketPrice = format(float(ticketPrice), ".2f")

                ticketDictionary[ticketZone] = {
                    "Capacity": zoneCapacity, "Price": ticketPrice
                }

                with open("Ticket.txt", "a") as file:
                    file.write(f"{ticketZone},{zoneCapacity},{ticketPrice}\n")

                print(ticketZone, "Zone added")
                break

    return ticketDictionary


def buyTicket():
    # os.system('cls')
    ticketDictionary = ticketMenu()
    bill = Bill()
    addedItem = False  # Item is empty

    while True:
        if not ticketDictionary:
            print("Ticket.txt is empty.")
            break
        else:
            print('\nTicket Available:')
            for i, ticketClass in enumerate(ticketDictionary.values(), start=1):
                print(f"{i}. {ticketClass}")

            selection = input(
                f"Enter selection from 1 to {i} (or 'q' to quit): ")
            if selection == "q":
                print("Buying process has been canceled")
                break
            else:
                if not selection.isdigit():
                    print("Invalid input. Please enter a number.")
                    continue

                selection = int(selection)
                if selection not in range(1, i + 1):
                    print(
                        f"Invalid ticket type. Please input selection from 1 to {i}.")
                    continue

                ticket = list(ticketDictionary.values())[selection - 1]
                if ticket.capacity == 0:
                    print("Ticket has sold out. Please choose another type of ticket.")
                    continue

                while True:
                    quantity = input("Enter the number of tickets: ")
                    if not quantity.isdigit() or int(quantity) <= 0:
                        print("Invalid input. Quantity must be a positive integer.")
                    else:
                        quantity = int(quantity)

                        if quantity > ticket.capacity:
                            print("Not enough tickets available. Please try again.")
                        else:
                            break

                bill.addItem(ticket, quantity)
                addedItem = True  # Set True thus an item is added

                # decrease quantity in ticket.txt file :) im going mentally insane
                with open("ticket.txt", "r") as file:
                    lines = file.readlines()

                with open("ticket.txt", "w") as file:
                    for line in lines:
                        data = line.strip().split(",")
                        if data[0] == ticket.zone:
                            updatedQuantity = max(0, int(data[1]) - quantity)
                            data[1] = str(updatedQuantity)
                        file.write(",".join(data) + "\n")

                while True:
                    continueSelection = input(
                        "Continue another purchase? (y/n): ")
                    if continueSelection.lower() == "y":
                        break
                    elif continueSelection.lower() == "n":
                        if addedItem:  # Check if any item is added to the bill
                            print("\n")
                            bill.printInvoice()
                        else:
                            print("No items added to the bill.")
                        return
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")


def showRecords():
    with open("bill.txt", "r") as file:
        file = file.readlines()
        if len(file) == 0:
            print('No billing records were found.')
        else:
            count = 0
            for line in file:
                count += 1
            print("Billing Records:")
            print("\n")
            print("Number of bills:", count)
            for line in file:
                print(
                    "---------------------------------------------------------------------")
                print("{:<10s}{:^25s}{:>10}".format(
                    "Bill No.", "Billing Date", "Total"))
                print(
                    "----------------------------------------------------------------------")
                billId, billDate, totalCharge = line.strip().split(",")
                billIdFormat = "B" + billId
                totalChargeFormat = "$" + totalCharge
                print("{:<10s}{:^25s}{:>10s}".format(
                    billIdFormat, billDate, totalChargeFormat))
                print(
                    "======================================================================")
                print("\n")
                print("\n")

# For exception handling and testing errors


def ticketMenuTestCheck():
    ticketDictionary = {}
    with open("ticket.txt", "r") as file:
        for line in file:
            ticketDetails = line.strip().split(",")
            if len(ticketDetails) == 3:
                ticketZone = ticketDetails[0]
                zoneCapacity = int(ticketDetails[1])
                ticketPrice = float(ticketDetails[2])
                ticketDictionary[ticketZone] = Ticket(
                    ticketZone, zoneCapacity, ticketPrice)

    for ticketZone, ticket in ticketDictionary.items():
        print(ticket)
        print(f"Ticket Zone: {ticketZone}")
        print(f"Capacity: {ticket.capacity}")
        print(f"Price: ${ticket.price:.2f}")
        print()
