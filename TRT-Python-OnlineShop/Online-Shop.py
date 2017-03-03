import time
import datetime


# Print List of each department with if, elif and else statements
# Define Departments

# global variables that contain dictionaries
hardware_list = {'phone': 299.00,'monitor': 150.00,}
software_list = {'Windows 10': 100.00,'Microsoft Office': 200.00, }
accessories_list = {'Keyboard': 29.00,'HDMI Gold-Plated': 49.00, }
warranties_list = {'1-year': 29.00,'2-year': 50.00, '2-year': 50.00,}

def get_department():
    # welcome message
    name = input("Please enter your name: ")
    print("Hello {}! Welcome to Cheap Tech Supplies".format(name))

    department_choice = None
    while department_choice != 5:
        print("Please enter 1, 2, 3, or 4 to pick a department or enter 5 to quit.\n")
        try:
            department_choice = int(input("1. Hardware\
                                   \n2. Software\
                                   \n3. Accessories\
                                   \n4. Warranties\
                                   \n\nChoose a department: \n"))

            if department_choice == 1:
                print(hardware_list)
                # hardware_selected = input("Welcome to Hardware, please choose an item")
            elif department_choice == 2:
                print(software_list)
                # software_selected = input("Welcome to Software, please choose an item")
            elif department_choice == 3:
                print(accessories_list)
                # software_selected = input("Welcome to Accessories, please choose an item")
            elif department_choice == 4:
                print(warranties_list)
                # software_selected = input("Welcome to Warranties, please choose an item")
            elif department_choice == 5:
                break

        except (ValueError):
            print("That is not a valid entry, please try again.\n")
            continue



get_department()




# online_shop = {}

# cart = []

# cart.append()

# Rawinput


#Find the price today
