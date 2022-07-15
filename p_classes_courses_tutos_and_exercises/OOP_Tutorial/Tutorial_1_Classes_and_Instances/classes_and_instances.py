# PYthon Object-Oriented Programming 

class Employee: 
    def __init__(self, first, last, pay, age, height): 
        self.first = first 
        self.last = first 
        self.pay = first  
        self.age = age 
        self.height = height 
        self.email = first + '.' + last + '@company.com' 

    def personalData(self, age, height): 
        self.age = age 
        self.height = height 
        self.dateOfBirth = 2021 - age 
        
        return self.dateOfBirth 


#########################################   Access Function   #########################################

emp_1 = Employee("Corey", "Schafer", 5000, 16, "1.76m") 
emp_2 = Employee("Test", "User", 6000, 57, "1.68m") 


def access(): 
    # Send values to the constructor's atributes to create object instances   
    answer = input('>>>> Which employee are you?: \n        a. Employee 1      b. Employee 2 \n\n>>>> Answer: ') 
    
    if answer == 'a': 
        print(f'>>>> Your height is {emp_1.height} and your age {emp_1.age}. Your date of birth is {emp_1.personalData(16, "1.74m")}') 
        print(f'>>>> Your email is: \'{emp_1.email}\'')

    if answer == 'b': 
        print(f'>>>> Your height is {emp_2.height} and your age {emp_2.age}. Your date of birth is {emp_2.personalData(57, "1.68m")}')  
        print(f'>>>> Your email is: \'{emp_2.email}\'') 

    elif (answer != 'a' or answer != 'b'): 
        raise Exception(f'¡An Exception Ocurred!\n>>>> No \'{answer}\' option or user...\n>>>> Please enter \'a\' or \'b\'') 

    print('\n') 


#########################################    Initializer   #########################################


if __name__ == '__main__': 
    print(end='\n')
    access()
    print(f'\n>>>> Instance Objects: Employee 1 = {emp_1}, Employee 1 = {emp_2}\n>>>> First employee email \'{emp_1.email}\', second employee email \'{emp_2.email}\'\n') 


"""
emp_1.first = "Corey"
emp_1.last = "Schafer" 
emp_1.email = "Corey.Schafer@company.com" 
emp_1.pay = 50000 

emp_2.first = "Test"
emp_2.last = "User" 
emp_2.email = "Test.User@company.com" 
emp_2.pay = 60000 

"""


