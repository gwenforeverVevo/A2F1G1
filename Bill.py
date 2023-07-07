import datetime
from Ticket import *

class Bill:
    count = 1
    def __init__(self):
        self.billId = Bill.count
        self.billDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.totalPrice = 0
        self.ticketItems = []
        Bill.count += 1

    def addItem(self, ticket, quantity):
        if ticket.capacity >= quantity:
            for item in self.ticketItems:
                if item[0] == ticket:
                    item[1] += quantity
                    item[2] = ticket.price * item[1]
                    break
            else:
                subtotal = ticket.price * quantity
                self.ticketItems.append([ticket, quantity, subtotal])
            
            self.totalPrice += ticket.price * quantity
            ticket.capacity -= quantity
        else:
            print("Insufficient capacity for the selected ticket type.")


    def billTotal(self):
        return self.totalPrice

    def printInvoice(self):
        print("-----------------------------------------------")
        print("{:^35s}".format("Invoice"))
        print("-----------------------------------------------")
        print("Date:", self.billDate)
        print("Bill No.:", self.billId)
        print("{:<15s}{:^10s}{:>10s}".format("Type","Qty","Subtotal"))
        print("-----------------------------------------------")
        for ticketItem in self.ticketItems:
            ticket, quantity, subtotal = ticketItem
            ticketType = ticket.zone
            print("{:<15s}{:^10d}{:>10.2f}".format(ticketType, quantity, subtotal))
        print("-----------------------------------------------")
        print("{:<15s}{:>20.2f}".format("Total",self.totalPrice))
        print("==============================================")
        with open("bill.txt", "a") as file:
            line = f"{self.billId},{self.billDate},{self.totalPrice}\n"
            file.write(line)
            # for ticketItem in self.ticketItems:
            #     ticket, quantity, subtotal = ticketItem
            #     ticketType = ticket.zone
            #     line = f"{self.billId},{self.billDate},{ticketType},{subtotal}\n"
            #     file.write(line)
            
    def getBillId(self):
        lastBillId = None
        with open("bill.txt", "r") as file:
            for line in file:
                billId, billDate, ticketZone, totalCharge = line.strip().split(",")
                lastBillId = billId
        return int(lastBillId) if lastBillId is not None else 0
               
            

