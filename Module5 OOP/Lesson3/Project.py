class Vehicle:
    def __init__(self, brand, speed):
        self.brand=brand
        self.speed=speed

    def show_details(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)

class Car(Vehicle):
    def __init__(self , brand,speed, doors):
        self.doors=doors
        super().__init__(brand, speed)

    def show_details(self):
        print("Cars🚘")
        print("Doors🪟:",self.doors)
        super().show_details()
car= Car("Toyota",180,4)
car.show_details()

class Bike(Vehicle):
    def __init__(self,brand, speed,gears):
        self.gears=gears
        super().__init__(brand, speed)

    def show_details(self):
       print("Bike🚲")
       print("Gears:",self.gears)
       super().show_details()

bike= Bike("Yamaha",120,6)
bike.show_details()

class Airplane(Vehicle):
    def __init__(self,brand,speed,seats):
        self.seats=seats
        super().__init__(brand,speed)

    def show_details(self):
        print("Airplane✈️")
        print("Seats:",self.seats)
        super().show_details()

airplane= Airplane("Boeing",900,300)
airplane.show_details()
