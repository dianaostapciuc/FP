from functions import generating_a_list_of_products, validating_add_command, adding_a_product_to_the_list, removing_a_product_from_list, sort_all_products_ascending_depending_on_price, sort_all_products_ascending_depending_on_quantity
def ui_start():

    list_of_products = []
    list_of_products = generating_a_list_of_products (list_of_products)
    
    while True:
        valid = False
        while not valid:
            try:

                print ("What would you like to do? ")
                command = input(">")
                if command == '0':
                    print ("The program is terminated :(.")
                    return

                current_command = command.split(" ")
                if current_command[0] == "add":
                    validating_add_command (current_command)
                    list_of_products = adding_a_product_to_the_list (list_of_products, current_command[1], current_command[2], current_command[3])
                elif current_command[0] == "remove":
                    list_of_products = removing_a_product_from_list (list_of_products, current_command[1], current_command[2])
                elif current_command[0] == "list":
                    if current_command[1] == "price":
                        list_of_products = sort_all_products_ascending_depending_on_price (list_of_products)
                        print (list_of_products)
                    elif current_command[1] == "quantity":
                        list_of_products = sort_all_products_ascending_depending_on_quantity (list_of_products)
                        print (list_of_products)
            except ValueError as ve:
                print("There was a " + str(type(ve)) + " " + str(ve))
            except TypeError as te:
                print("There was a " + str(type(te)) + " " + str(te))
            except IndexError as ie:
                print("There was a " + str(type(ie)) + " " + str(ie))
            except AssertionError as ae:
                print ("There was a " + str(type(ae)) + " " + str(ae))
            else:
                print("The input command is valid")

            finally:
                print("continuing to run...")

            valid = True
    
                    
ui_start()