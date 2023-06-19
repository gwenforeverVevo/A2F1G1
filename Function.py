import sys

def mainMenu():
    # generates the main menu information and stores the data in a dictionary, 
    # return the menu dictionary
    menuDictionary = {"1": "Add ticket", "2": "Buy ticket", "3": "Show Records", "4": "Quit"}
    
    print("*****BTS Concert*****\n")
    print("Function menu:")
    
    for key, value in menuDictionary.items():
        print(f"{key}. {value}")

    inputMenu =str(input("\nEnter selection (1-4): "))
    match inputMenu:
        case "1":
            addNewTicket()
        case "2":
            buyTicket()
        case "3":
            showRecords()
        case "4":
            print('\nThank you for using the system.\n')
            sys.exit()
        case "5":
            print('\nThank you for using the system.\n')
            sys.exit()
        case _:
            print("\nError, Input the correct Value!")

    return menuDictionary, inputMenu 
            
def ticketMenu():
    # – generate available ticket type for selection by reading the data from ticket.txt 
    # file and store the data into a dictionary. Return the dictionary
    print('lol')
    
    
def addNewTicket():
    # reads data needed from user and appends the record into the ticket.txt file
    ticketDictionary = {}
    ticketZone = str(input("Enter ticket zone: "))
    zoneCapacity = str(input("Enter zone capacity: "))
    ticketPrice = str(input("Enter price: "))

    ticketDictionary[ticketZone] = {"Capacity": zoneCapacity, "Price": ticketPrice}
    #ticketDictionary=object [ticketZone]=key
    
    with open("ticket.txt", "a") as file: #"a"=append
        file.write(f"{ticketZone}, {zoneCapacity}, {ticketPrice}")
    print(ticketZone , "Zone added")

    return ticketDictionary
    
def buyTicket():
    # o create bill object
    # o loop to allow user to buy multiple tickets by reading the ticket type and 
    # number of tickets each round. For each ticket type added, update the bill 
    # object.
    # o ticket menu is displayed by using the dictionary returned from ticketMenu
    # function
    # o print bill invoice at the end. Use printInvoice function created in class Bill
    # o store the bill data into bill.txt fil
    print("lol")

def showRecords():
    # showRecords – reads data from bill.txt file and show the data of each bill.
    print("Ticket avaible")