class user:
    def __init__(self,fname,lname,number):
        self.fname = fname
        self.lname = lname
        self.number = number
    fname = ''
    lname = ''
    number = ''

class employee(user):
    empID = ''
    salary = ''

class manager(user):
    empID = ''
    department = ''
    salary = ''

user1 = user('Bob', 'Moore', 5555555)


print("name: {} {}, number: {}".format(user1.fname,user1.lname,user1.number))

emp1 = employee('Bill','Billiard',9999999)

print("name: {} {}, number: {}".format(emp1.fname,emp1.lname,emp1.number))

emp1.empID = 12345

print(emp1.empID)
