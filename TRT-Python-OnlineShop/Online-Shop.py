import time
import datetime

#This is the first comment

# today = datetime.datetime.dayofweek()

# Raw Input "Welcome Message to Cheap Tech Supplies"

name = input("Please enter your name: ")

welcome = print("Hello {}! Welcome to Cheap Tech Supplies".format(name))

departmentChoice = int(input("1. Hardware\
                   \n2. Software\
                   \n3. Accessories\
                   \n4. Warranties\
                   \n\nChoose a department: \n"))

### Print List of each department with if, elif and else statements
### Define Departments

hardwareList = {'phone': 299.00,'monitor': 150.00,}
softwareList = {'Windows 10': 100.00,'Microsoft Office': 200.00, }
accessoriesList = {'Keyboard': 29.00,'HDMI Gold-Plated': 49.00, }
warrantiesList = {'1-year': 29.00,'2-year': 50.00, '2-year': 50.00,}

def getDepartment(departmentChoice):
    if departmentChoice == 1:
        print(hardwareList)
        hardwareSelected = input("Welcome to Hardware, please choose an item")
    elif departmentChoice == 2:
        print(softwareList)
        softwareSelected = input("Welcome to Software, please choose an item")
    elif departmentChoice == 3:
        print(accessoriesList)
        softwareSelected = input("Welcome to Accessories, please choose an item")
    elif departmentChoice == 4:
        print(warrantiesList)
        softwareSelected = input("Welcome to Warranties, please choose an item")
    else:
        print("Not a valid selection, please choose a number")

getDepartment(departmentChoice)




# online_shop = {}

# cart = []

# cart.append()

# Rawinput


#Find the price today
