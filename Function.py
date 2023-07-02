import sys
import os
from Ticket import *
from Bill import *
import datetime


def mainMenu():
    # generates the main menu information and stores the data in a dictionary,
    # return the menu dictionary
    open('bill.txt', 'w').close() #clear the contents of the bill.txt file whenever a new user uses this system.
    menuDictionary = {"1": "Add ticket", "2": "Buy ticket",
                      "3": "Show Records", "4": "Quit"}
    os.system('cls')
    print("*****BTS Concert*****\n")
    while (True):
        
        print("\nFunction menu:")

        for key, value in menuDictionary.items():
            print(f"{key}. {value}")

        inputMenu =  (input("\nEnter selection (1-4): "))
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
                # Error handerling
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
    os.system('cls')
    # reads data needed from user and appends the record into the ticket.txt file
    ticketDictionary = {}
    ticketZone = str(input("Enter ticket zone: "))
    zoneCapacity = int(input("Enter zone capacity: "))
    ticketPrice = float(input("Enter price: "))
    ticketDictionary[ticketZone] = {
        "Capacity": zoneCapacity, "Price": ticketPrice}
    # ticketDictionary=object [ticketZone]=key
    with open("Ticket.txt", "a") as file:  # "a"=append
        file.write(f"{ticketZone},{zoneCapacity},{ticketPrice}\n")
    print(ticketZone, "Zone added")
    os.system('cls')
    return ticketDictionary


def buyTicket():
    os.system('cls')
    ticketDictionary = ticketMenu()
    bill = Bill()
    
    while True:
        print('\nTicket Available:')
        for i, (ticketZone, ticketClass) in enumerate(ticketDictionary.items(), start=1):
            print(f"{i}. {ticketClass}")

        selection = input("Enter selection (or 'q' to quit): ")
        if selection == "q":
            break

        if selection is None:
            print("Invalid ticket type. Please try again.")
            break
        else:
            selection = int(selection)

        if selection not in range(1, len(ticketDictionary) + 1):
            print("Invalid ticket type. Please try again.")
            continue

        ticket = list(ticketDictionary.values())[selection - 1]
        quantity = int(input("Enter the number of tickets: "))

        if quantity > ticket.capacity:
            print("Not enough tickets available. Please try again.")
            continue
            
        bill.addItem(ticket, quantity)

        # Decrease quantity in ticket.txt file
        with open("ticket.txt", "r") as file:
            lines = file.readlines()

        with open("ticket.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == ticket.zone:
                    updated_quantity = max(0, int(data[1]) - quantity)
                    data[1] = str(updated_quantity)
                file.write(",".join(data) + "\n")

        continueSelection = input("Continue another purchase? (y/n): ")
        if continueSelection == "y":
            continue
        elif continueSelection == "n":
            break
        else:
            print("Invalid input. Please try again.\n\n")
    print("\n\n")
    bill.printInvoice()



def showRecords():
    with open("bill.txt", "r") as file:
        file=file.readlines()
        if len(file) == 0:
            print('No billing records were found.')
        else:
            print("Billing Records:")
            print("\n")
            print("\n")
            print("Number of bills:")
            for line in file:
                print("---------------------------------------------------------------------")
                print("{:<10s}{:^25s}{:>10}".format("Bill No.","Billing Date","Total"))
                print("----------------------------------------------------------------------")
                billId, billDate, totalCharge = line.strip().split(",")
                billIdFormat = "B" + billId
                totalChargeFormat = "$" + totalCharge
                print("{:<10s}{:^25s}{:>10s}".format(billIdFormat,billDate,totalChargeFormat))
                print("======================================================================")
                print("\n")
                print("\n")

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
