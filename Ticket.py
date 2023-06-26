class Ticket:
    def __init__(self, zone, capacity, price):
        self.zone = zone
        self.capacity = int(capacity)
        self.price = float(price)

    def __str__(self):
        return f"{self.zone} (${self.price})"
 