#Cash Register Program
#Author: Christian Eriksen
#Program can do stuff

#Import modules
import RetailItem
#import CashReg
import time

# Constants for the menu choices
SHOW_ITEMS = 1
PURCHASE_ITEM = 2
GET_TOTAL = 3
CLEAR = 4
QUIT_CHOICE = 5

#FILENAME = 'employee.dat'

#The main function.
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0
    retail_items ={}
    infolist = {
     1:['Jacket', 12, 59.95],
     2:['Designer Jeans', 40, 34.95],
     3:['Shirt', 20, 24.95]
    }#end of list
    for keys in infolist:
        retail_items[keys] = RetailItem.RetailItem((infolist[keys])[0], (infolist[keys])[1], (infolist[keys])[2])
    print(retail_items)
    for n in range(1,4):#Create three instances of class and print them
        self = RetailItem.RetailItem((infolist[n])[0], (infolist[n])[1], (infolist[n])[2])	
        print('Item #',n)
        print('Description\t   : ', self.get_description())
        print('Amount in inventory: ', self.get_units_in_inv())
        print('price\t\t   : ', self.get_price(),'\n')
    print(self)	
    while choice != QUIT_CHOICE:
        # display the menu.
        print('Welcome to Cash Register Program')
        print('-'*7,'MENU','-'*7)
        print('1) Show all purchasable items')
        print('2) Purchase an Item')
        print('3) Show total')
        print('4) Clear the list of purchased items')
        print('5) Quit')

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == SHOW_ITEMS:
            print('Displaying Items:')
            find_employee(employee_db)
        elif choice == PURCHASE_ITEM:
            print('Which item woul you like to purchase?')
            add_employee()
        elif choice == GET_TOTAL:
            print('Your purchases summed up to')
            golf_read()
        elif choice == CLEAR:
            print('Clearing list of purchased items')
            golf_read()
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
            time.sleep(2)#using the sleep function so the program does not exit instantly
            exit()
        else:
            print('Error: invalid selection.\n')

def load_employees():
    try:
        # Open the contacts.dat file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        contact_dct = pickle.load(input_file)

        # Close the phone_inventory.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        contact_dct = {}

    # Return the dictionary.
    return contact_dct
 


def find_employee(employee_db):#Employee search function is defind here
    #Defining accumulators, total and number of lines
    Search_ID = input('Type ID of employee you wish to search for:\n')
    print(employee_db.get(Search_ID, 'Not Found'))

def remove_this_line():
    if Search_ID in employee_db:
        print('Tournament Record Holders of Springfork Amateur Golf Club :')
        print()
        print('Name\tScore')
        print('----------------------------------')
        for line in golf_in:
            line = line.rstrip('\n')
            counter += 1
            print(line)
        golf_in.close()# Close the file.
        # Print the total.
        print()
        #print('Number of players in the file: ', counter)
    else:
        print('Employee ID not found')

def add_employee():#lookup function is defined here
    go_on = 'y'
    try:
        add_record = input("Add a new record? : ('y' for yes, any other button for no.)")
        if add_record == 'y':
           record_no = input('Please type the name or number of the record: ')
           employee_db = pickle.load('employee.dat', 'rb')
           golf_out.write('\nTournament ' + str(record_no)+'\n')
           while go_on == 'y':
              player_name = input('Please enter name of player: ')
              player_score = input('Please enter score of player: ')
              outline = str(player_name + '\t' + player_score + '\n')
              golf_out.write(outline)
              go_on = input("type 'y' to add another record: ")
           else:
              print('Ending input')
              golf_out.write('-end of record-\n\n')
        else:
           golf_out.close()
           exit()
    except IOError as err:
        print(err)
        golf_out.close()

def add_employee():#lookup function is defined here
    go_on = 'y'
    try:
        add_record = input("Add a new record? : ('y' for yes, any other button for no.)")
        if add_record == 'y':
           record_no = input('Please type the name or number of the record: ')
           employee_db = pickle.load('employee.dat', 'rb')
           golf_out.write('\nTournament ' + str(record_no)+'\n')
           while go_on == 'y':
              player_name = input('Please enter name of player: ')
              player_score = input('Please enter score of player: ')
              outline = str(player_name + '\t' + player_score + '\n')
              golf_out.write(outline)
              go_on = input("type 'y' to add another record: ")
           else:
              print('Ending input')
              golf_out.write('-end of record-\n\n')
        else:
           golf_out.close()
           exit()
    except IOError as err:
        print(err)
        golf_out.close()

# Call the main function.
main()
