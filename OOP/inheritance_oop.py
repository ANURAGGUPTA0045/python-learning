class user:                         #parent class
    def __init__(self):
        self.name = 'anurag'

    def login(self):
        print("user logged in")     

class student(user):               #child class
   
    def enroll(self):
        print("student enrolled")

u = user()
s = student()

print(s.name)
s.enroll()
s.login()