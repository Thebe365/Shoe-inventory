# Shoe inventory system
### A small example of a shoe inventory system
This applications makes use of OOP principals, reads, and writes data to a text file.

The project performs the following functions:
### Reads shoe data from a file
Reads shoe data from file, creates an object for each shoe and stores the objects into a list

### Captures a shoe
Prompts the user to enter information related to a shoe they'd like to capture, creates an
object of the shoe, then stores it in the shoe list and writes the shoe data to a file

### View all shoes
Displays all the shoes in the list in a readable format

### Restock shoe
This function looks for a shoe with the lowest quantity in the list, prompts the user if they'd like to
restock the shoe or not. If they choose yes, the program prompts the user to enter the number of shoes
they'd like to add then updates the shoe object's quantity in the list and updates the shoe file

### Search shoe
allows the user to search for a shoe by its index then displays the shoe's information by displaying
it in a readable format

### Items value
Displays the total value of each shoe in the inventory by multiplying each shoe's price by its quantity

### Display shoe on sale
Displays a shoe with the highest quantity and displays it as being on sale
