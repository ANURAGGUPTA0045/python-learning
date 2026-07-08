class Animal:
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):

        print("Dog barks")


class cats(Animal):

    def sound(self):
        print("cat meows")



a = Animal()
b = cats()
c = Dog()

b.sound()
c.sound()
    