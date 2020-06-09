# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# RRoot,1.1.2020,Added pseudo-code to start assignment 8
# AAsgekar,6.8.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #




# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AAsgekar,6.8.2020,Modified code to complete assignment 8
    """
   # --Constructor --
    def __init__(self, product_name, product_price):
        # --Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # --Properties --
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self,value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else: raise Exception("Product Name cannot be a number.")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        self.__product_price = float(value)
# Data -------------------------------------------------------------------- #




# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AAsgekar,6.8.2020,Modified code to complete assignment 8
    """

    # --Methods --
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Saves data from a list of dictionary rows to a file

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: feedback statement for the user
        """
        objFile = open(file_name, "w")
        for row in list_of_product_objects:
            objFile.write(row["Name"] + ", " + str(row["Price"]) + "\n")
        objFile.close()
        feedback = "Your data has been saved."
        return feedback

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_product_objects.clear()  # clear current data
        objFile = open(file_name, "r")
        for line in objFile:
            name, price = line.split(",")
            row = {"Name": name.strip(), "Price": price.strip()}
            list_of_product_objects.append(row)
        objFile.close()
        return list_of_product_objects, 'Success'

    @staticmethod
    def add_data_to_list(name, price, list_of_product_objects):
        """Adds data to a list

        :param name: (string) with name of task:
        :param price: (string) with name of priority:
        :param list_of_product_objects: (list) you want to add data to
        :return: (list) of dictionary rows
        """
        dicRow = {"Name": name, "Price": price}
        list_of_product_objects.append(dicRow)
        return list_of_product_objects, 'Success'
# Processing  ------------------------------------------------------------- #




# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Displays output to user and receives user inputs:

    methods:
        menu():

        menu_choice(): -> (string)

        print_current_inventory(list_of_product_objects):

        user_input_product_name(): -> (string) name

        user_input_product_price(): -> (string) price

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AAsgekar,6.8.2020,Modified code to complete assignment 8
    """
    # --Methods --
    @staticmethod
    def menu():
        """ Displays menu to the user

        :return: nothing
        """
        print \
        ("""
        
        Product Inventory
        
        1 - View current product inventory
        2 - Add a product to inventory
        3 - Save data and exit program
        
        """)

    @staticmethod
    def menu_choice():
        """ Gets user's menu selection

        :return: (string) choice
        """
        choice = input("Please select a menu option: ")
        return choice

    @staticmethod
    def print_current_inventory(list_of_product_objects):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_product_objects: (list) of rows you want to display
        :return: nothing
        """
        if list_of_product_objects == []:
            print("There is currently nothing in the Product Inventory.")
        else:
            print("The current Product Inventory is:")
            for row in list_of_product_objects:
                print(row["Name"] + " (" + str(row["Price"]) + ")")

    @staticmethod
    def user_input_product_name():
        """ Gets user input for Product Name

        :return: (string) name
        """
        name = input("Enter Product Name: ")
        return name

    @staticmethod
    def user_input_product_price():
        """ Gets user input for Product Price

        :return: (string) price
        """
        price = input("Enter Product Price: ")
        return price
# Presentation (Input/Output)  -------------------------------------------- #




# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
try:
    FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
except FileNotFoundError:
    #create the file if it didn't already exist
    FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)


user_choice = " "
while user_choice != None:
# Show user a menu of options
    IO.menu()
# Get user's menu option choice
    user_choice = IO.menu_choice()

# Show user current data in the list of product objects
    if user_choice == "1":
        print()
        IO.print_current_inventory(lstOfProductObjects)
        input("Press enter to return to the menu.")

# Let user add data to the list of product objects
    elif user_choice == "2":
        print()
        p1 = Product("Product", 0)
        try:
            #test that input obeys properties
            p1.product_name = IO.user_input_product_name()
        except Exception as e:
            print(e)
            input("Press enter to return to the menu.")
            continue
        try:
            #test that input obeys properties
            p1.product_price = IO.user_input_product_price()
            FileProcessor.add_data_to_list(p1.product_name,p1.product_price,lstOfProductObjects)
            print("Your data has been added to the list.")
            input("Press enter to return to the menu.") 
        except ValueError:
            print("Price entered was not a number.")
            input("Press enter to return to the menu.")
            continue

# let user save current data to file and exit program
    elif user_choice == "3":
        print()
        print(FileProcessor.save_data_to_file(strFileName,lstOfProductObjects))
        print("Thank you for using the program.")
        input("Press enter to exit.")
        break

    else:
        print()
        print("That was not a menu item.")
        print("Please select 1, 2 or 3.")
        input("Press enter to return to the menu.")
# Main Body of Script  ---------------------------------------------------- #