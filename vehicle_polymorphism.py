class Vehicle():

    def start(self):

        print("lets go")

class Car(Vehicle):
    def start(self):
        print("car started")

class Bike(Vehicle):
    def start(self):
        print("bike started")

a = Car()
b = Bike()
c = Vehicle()
a.start()
b.start()
c.start()


