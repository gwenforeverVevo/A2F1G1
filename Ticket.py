class Ticket:
    def __init__(self, zone, capacity, price):
        self.zone = zone
        self.capacity = int(capacity)
        self.price = float(price)

    def __str__(self):
        if self.capacity == 0:
            return "{:<15s} (${:<5.2f}) - SOLD OUT!!".format(self.zone, self.price)
        else:
            return "{:<15s} (${:<5.2f}) ".format(self.zone, self.price)
 