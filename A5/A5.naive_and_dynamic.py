"""
    3. Length and elements of a longest subarray of numbers having increasing modulus.
    (naive implementation)
    11. The length and elements of a maximum subarray sum, when considering each number's real part.
    (dynamic implementation)
"""
from math import sqrt
# LIST:

def get_real_part_of_number(element):
    return element [0]

def get_imaginary_part_of_number(element):
    return element [1]

def create_a_complex_number_to_add (list_of_complex_numbers, real_part, imaginary_part):
    list_of_complex_numbers.append([real_part, imaginary_part])
 


#DICTIONARY:
# def get_real_part_of_number(element):
#    return element ['real']

# def get_imaginary_part_of_number(element):
#     return element ['imag']

# def create_a_complex_number_to_add (list_of_complex_numbers, real_part, imaginary_part):
#     dictionary = {}
#     dictionary ['real'] = real_part
#     dictionary ['imaginary'] = imaginary_part
#     list_of_complex_numbers.append(dictionary)

# works for both:

def transform_into_string (element):

    real_part = str(get_real_part_of_number(element))
    negative_imaginary = False
    if get_imaginary_part_of_number(element) < 0:
        negative_imaginary = True

    imaginary_part = str(get_imaginary_part_of_number(element))

    if negative_imaginary == True:
        transformed_string = "(" + real_part + imaginary_part + "i" + ")"
    else: 
        transformed_string = "(" + real_part + "+" + imaginary_part + "i" + ")"
    return transformed_string
   

#THE REST OF THE CODE HERE:

def read_the_list (length_list, list_of_complex_numbers):

    for i in range (length_list):
        print ("A complex number can be written as z = a + bi")
        real_part = int(input ("The value for a is: "))
        imaginary_part = int(input ("The value for b is: "))
        create_a_complex_number_to_add (list_of_complex_numbers, real_part, imaginary_part)

def transform_a_list_into_a_string (list_of_complex_numbers, length_list):
    
    transformed_string = '['
    for i in range (length_list):
        tranformed_element = transform_into_string (list_of_complex_numbers[i])
        transformed_string += tranformed_element
        if i != length_list - 1:
            transformed_string += ','
    transformed_string += ']'
    return transformed_string


def display_the_list_of_complex_numbers (list_of_complex_numbers, length_list):

    string_list_of_complex_numbers = transform_a_list_into_a_string(list_of_complex_numbers, length_list)
    print (string_list_of_complex_numbers)


def calculating_the_modulus_of_a_complex_number (element):

    real_part = get_real_part_of_number(element)
    imaginary_part = get_imaginary_part_of_number(element)
    modulus = sqrt(real_part*real_part + imaginary_part*imaginary_part)
    return modulus

def making_an_array_with_every_numbers_modulus (list_of_complex_numbers, length_list):

    array_with_modulus = []
    for i in range (length_list):
        modulus = calculating_the_modulus_of_a_complex_number (list_of_complex_numbers[i])
        array_with_modulus.append (modulus)
    return array_with_modulus

def determining_the_longest_subarray_with_increasing_modulus_by_checking_every_modulus_of_each_number (list_of_complex_numbers, length_list):
     
    array_containing_modulus = []
    array_containing_modulus = making_an_array_with_every_numbers_modulus (list_of_complex_numbers, length_list)
    maximum_value_of_the_subarray = -1
    count_increasing_elements = 1
    for i in range (1, len(array_containing_modulus)):
        if array_containing_modulus[i] >= array_containing_modulus [i-1]:
            count_increasing_elements += 1
        else:
            if count_increasing_elements > maximum_value_of_the_subarray:
                maximum_value_of_the_subarray = count_increasing_elements
                ending_index_of_subarray = i-1
                starting_index_of_subarray = i - count_increasing_elements
            count_increasing_elements = 1
    print ("The subarray is: " + str(list_of_complex_numbers [starting_index_of_subarray:ending_index_of_subarray+1]))
    return maximum_value_of_the_subarray

def determining_the_maximum_sum_of_a_subarray_depending_on_the_real_part_of_a_complex_number (list_of_complex_numbers):

    maximum_value_of_sum = 0
    maximum_length_of_subarray = 0
    current_sum = 0
    length_of_subarray = 0 
    for i in range (len(list_of_complex_numbers)):

        real_part = get_real_part_of_number(list_of_complex_numbers[i])

        if current_sum + real_part > 0:
            current_sum+=real_part
            length_of_subarray+=1
        else:
            current_sum = 0
            length_of_subarray = 0
        if current_sum > maximum_value_of_sum:
            maximum_value_of_sum = current_sum
            maximum_length_of_subarray = length_of_subarray
            starting_index_of_subarray = i - maximum_length_of_subarray + 1
    print ("The sum is: "+str(maximum_value_of_sum))
    print ("The maximum length is: " + str (maximum_length_of_subarray))
    print ("The maximum sum subarray is" + str(list_of_complex_numbers[starting_index_of_subarray:starting_index_of_subarray+maximum_length_of_subarray]))


def menu ():

    list_of_complex_numbers = [[2,3],[5,4],[-1,2],[6,5],[7,4],[-8,5],[3,4],[2,1],[-16,5],[2,2]]
 #  list_of_complex_numbers = [{'real': 2, 'imag': 3}, {'real': 5, 'imag': 4}, {'real': 1, 'imag': 2}, {'real': 6, 'imag':5}, {'real': 7, 'imag': 4}, {'real': 8, 'imag':5}, {'real': 3, 'imag': 4}, {'real': 2, 'imag': 1}, {'real': 6, 'imag': 5}, {'real': 2, 'imag': 2}]
    additional_numbers = int(input ("How many additional numbers would you like to work with? "))
    count_for_complex_numbers = additional_numbers + 10
    
    while True:
        print ("What would you like to do?")
        print ("1. Read and create the list.")
        print ("2. Display the entire list. ")
        print ("3. Display longest subarray of numbers having increasing modulus.")
        print ("4. Display the length and elements of a maximum subarray sum, when considering each number's real part. ")
        print ("5. Exit the program.")

        choice = input (">")

        if choice == "1":
            read_the_list (additional_numbers, list_of_complex_numbers)
        elif choice == "2":
            display_the_list_of_complex_numbers (list_of_complex_numbers, count_for_complex_numbers)
        elif choice == "3":
            maximum_value_of_subarray = determining_the_longest_subarray_with_increasing_modulus_by_checking_every_modulus_of_each_number (list_of_complex_numbers, count_for_complex_numbers)
            print ("The maximum value of the subarray is: " + str(maximum_value_of_subarray))
        elif choice == "4":
            determining_the_maximum_sum_of_a_subarray_depending_on_the_real_part_of_a_complex_number (list_of_complex_numbers)
        elif choice =="5":
            return
        else: print ("Bad command!")

menu ()