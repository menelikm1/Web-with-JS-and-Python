class Flights:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def book_flight(self, name):
        if self.check_seats():
            self.passengers.append(name)
            return True
        else:
            # print(f"No available seats for {name}")
            print("no available seats for " + name)
            return
    def check_seats(self):
        if self.capacity - len(self.passengers) > 0:
            return True
        else:
            return False

flight = Flights(3)

peeps = ["Me", "Her", "Him", "Us"]

for i in peeps:
    flight.book_flight(i)
    print("successfully added " + i)
print(flight.passengers)