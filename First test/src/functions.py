import random

def validating_add_command (current_command):

    if len(current_command) != 4:
        raise ValueError ("Invalid length of command!")
    if int(current_command[2]) <0 or int(current_command[3]) <0:
        raise ValueError ("Invalid values!")

def tests_for_functionality_remove ():

    test_list = []
    test_list = generating_a_list_of_products (test_list)
    assert (removing_a_product_from_list (test_list, '>', 120) != test_list), "The removing function doesn't work properly"
    assert (removing_a_product_from_list (test_list, '<', 450) != test_list), "The removing function doesn't work properly"
    assert (removing_a_product_from_list (test_list, '>', 120) != test_list), "The removing function doesn't work properly"
# ----------------------------------------------------------------
def generating_a_list_of_products (list_of_products):

    product_names = ["Napkins", "Tea", "Potato", "Apple"]

    for i in range (5):
        current_product = []
        current_product.append(product_names[random.randint(0,3)])
        current_product.append (random.randint (1,500))
        current_product.append (random.randint (1,20))
        list_of_products.append(current_product)

    print (list_of_products)
    return list_of_products

def comparing_values_with_a_given_comparison_sign (value1, value2, comparison_sign):

    if comparison_sign == ">":
        if value1 > value2:
            return True
    elif comparison_sign == "<":
        if value1 < value2:
            return True
    return False

# ----------------------------------------------------------------

def adding_a_product_to_the_list (list_of_products, name, quantity, item_price):

    current_product = []
    current_product.append(name)
    current_product.append(int(quantity))
    current_product.append(int(item_price))
    list_of_products.append(current_product)
    return list_of_products

def removing_a_product_from_list (list_of_products, comparison_sign, given_value):
    
    for prod in list_of_products:
        if comparing_values_with_a_given_comparison_sign (int(prod[1]), int(given_value), comparison_sign) == True:
            number_of_elements = 3
            while number_of_elements != 0:
                prod.pop ()
                number_of_elements -= 1
            number_of_elements = 3
            while number_of_elements != 0:
                prod.append (0)
                number_of_elements -= 1

    return list_of_products

def sort_all_products_ascending_depending_on_price (list_of_products):

    for i in range (len(list_of_products)):
        j = i+1
        for j in range (len(list_of_products)):
            if int(list_of_products[i][1]) < int(list_of_products[j][1]):
                list_of_products[i], list_of_products[j] = list_of_products[j], list_of_products[i]
    return list_of_products

def sort_all_products_ascending_depending_on_quantity (list_of_products):

    for i in range (len(list_of_products)):
        j = i+1
        for j in range (len(list_of_products)):
            if int(list_of_products[i][2]) < int(list_of_products[j][2]):
                list_of_products[i], list_of_products[j] = list_of_products[j], list_of_products[i]
    return list_of_products



