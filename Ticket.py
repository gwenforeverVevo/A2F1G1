class Ticket:
    def __init__(self, zone, capacity, price):
        self.zone = zone
        self.capacity = int(capacity)
        self.price = float(price)

    def __str__(self):
        if self.capacity == 0:
            return f"{self.zone} (${self.price:.2f}) - SOLD OUT!!"
        else:
            return f"{self.zone} (${self.price:.2f})"
 