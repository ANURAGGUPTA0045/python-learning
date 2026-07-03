class customer:
    def __init__(self,name,gender,age,address):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address

    def print_address(self):
        print(self.address.city,self.address.pin,self.address.state)

    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)



class address:
    def __init__(self,city,pin,state):
        self.city = city
        self.pin = pin
        self.state = state

    def edit_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state

add1 =address("mumbai",1234,"maharashtra")
cust1 = customer("anurag","male",19,add1)

cust1.print_address()

cust1.edit_profile("anurag","pune",5678,"maharashtra")
cust1.print_address()