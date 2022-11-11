# Shoes class
class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Get cost of shoe
    def get_cost(self):
        return self.cost

    # Get quantity of shoe
    def get_quanty(self):
        return self.quantity

    # return a string representation of class
    def __str__(self):
        return f"\nCountry:\t\t{self.country}\nCode:\t\t\t{self.code}\nProduct:\t\t{self.product}\nCost:\t\t\tR {self.cost}\nQuantity:\t\t{self.quantity}"



# Read shoes function
def read_shoes_data():

    try:

        # open inventory file and read data
        shoe_file = open("inventory.txt", "r")
        shoe_data = shoe_file.readlines()
        
        # Read each line in file and create new shoe object
        for i in range(1, len(shoe_data)):

            line = shoe_data[i].strip("\n")
            line = line.split(",")
            shoe = Shoes(line[0], line[1], line[2], line[3], line[4])
            shoe_list.append(shoe)
        
        # close file
        shoe_file.close()
        return shoe_list
    except FileNotFoundError as error:

        print(error)


# capture shoe
def capture_shoes(country, code, prod, cost, quan):

    # create a new shoe object and append to shoes list
    shoe = Shoes(country, code, prod, cost, quan)
    shoe_list.append(shoe)
    
    # Write shoe to inventory file
    try:

        inv_file = open("inventory.txt", "a")
        inv_file.write("\n" + country + "," + code + "," + prod + "," + cost + "," + quan)
        return shoe

    except FileNotFoundError as error:
        return error


# View all
def view_all(shoe_list):
    
    for shoe_obj in shoe_list:
        print(shoe_obj)

# restock product
def re_stock(shoe_list):

    quan_list = []

    # Get all shoes' quantity
    for shoe_obj in shoe_list:
        quan_list.append(int(shoe_obj.get_quanty()))

    # Find lowest value in list then find it's index
    small_val = min(quan_list)
    small_ind = quan_list.index(small_val)
    print(shoe_list[small_ind])

    # prompt user if they'd like to restock the shoe
    restock_opt = input("Would you like to restock the shoe?(Yes or No): ").lower()

    if restock_opt == "yes":

        # Update shoe quantity
        prev_quan = int(shoe_list[small_ind].get_quanty())
        quan_amount = int(input("How many shoes would you want to restock: "))
        new_quan = prev_quan + quan_amount
        shoe_list[small_ind].quantity = str(new_quan)

        try:

            # Update inventory file with new data
            inv_file = open("inventory.txt", "r+")
            inv_data = inv_file.readlines()

            updated_line = shoe_list[small_ind].country + "," + \
                            shoe_list[small_ind].code + "," + \
                            shoe_list[small_ind].product + "," + \
                            shoe_list[small_ind].cost + "," + \
                            shoe_list[small_ind].quantity + "\n"

            inv_data[small_ind + 1] = updated_line

            # Open inventory file and update its data
            inv_file = open("inventory.txt", "w")
            inv_file.writelines(inv_data)

            # Close file
            inv_file.close()
            print("Stock has been updated updated!")

        except FileNotFoundError as error:
            print(error)


# Search shoe in inventory
def search_shoe(item, shoe_list):

    item_found = False

    # Search for shoe and makr item_found as true if  found
    for shoe_obj in shoe_list:

        if item == shoe_obj.product.lower():
            item_found = True
            found_item = shoe_obj
    
    # Return shoe object if found  
    if item_found == True:
        return found_item
    else:
        return "Item not found"

# item value
def value_per_item(shoe_list):
    
    for shoe_obj in shoe_list:
        value = int(shoe_obj.get_cost()) * int(shoe_obj.get_quanty())
        print(shoe_obj.product + " = R" + str(value))

# highest quantity
def highest_qty(shoe_list):
    
    quan_list = []

    for shoe_obj in shoe_list:
        # print(shoe_obj.get_quanty())
        quan_list.append(int(shoe_obj.get_quanty()))

    big_val = max(quan_list)
    big_ind = quan_list.index(big_val)
    return shoe_list[big_ind]

shoe_list = []

# Main program function
def main():

    # Call the read shoes function
    read_shoes_data()
    option = ""

    while option != 7:

        option = int(input("""Select option - 
                        capture shoe - 1
                        view shoes - 2
                        restock - 3
                        search shoe - 4
                        value per item - 5
                        Shoe on sale - 6
                        Quit - 7: """))
        
        if option == 1:

            # Prompt user for shoe data
            country = input("Enter country: ").capitalize()
            code = input("Enter shoe code: ").upper()
            product = input("Enter shoe name: ").capitalize()
            cost = input("Enter shoe price: ")
            quan = input("Enter shoe Quantity: ")

            # Create shoe object
            print(capture_shoes(country, code, product, cost, quan))

        elif option == 2:

            # Display all shoes in list
            view_all(shoe_list)

        elif option == 3:

            # Get shoe object that has the lowest quantity
            re_stock(shoe_list)

        elif option == 4:

            # prompt user to enter the shoe they are looking for
            item_search = input("Enter name of shoe to search: ").lower()
            
            # Print search result
            print("Search results:")
            print("========================")
            print(search_shoe(item_search, shoe_list))
        
        elif option == 5:
            
            # Display value per shoe
            print(value_per_item(shoe_list))

        elif option == 6:
            
            # print shoe with highest quantity as on sale
            print("Shoe on sale")
            print("========================")
            print(highest_qty(shoe_list))
        elif option == 7:
            print("Goodbye!")
        else:
            print("Invalid selection!")

# Call main function
main()