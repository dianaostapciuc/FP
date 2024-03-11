""" 
    Given the set of positive integers S, partition this set into two subsets S1 and S2
    so that the difference between the sum of the elements in S1 and S2 is minimal.
    For example, for set S = { 1, 2, 3, 4, 5 }, the two subsets could be S1 = { 1, 2, 4 }
    and S2 = { 3, 5 }. Display at least one of the solutions.

"""
def reading_a_list_of_elements ():

    list = []
    length = int(input ("What's the length of your list? "))
    for i in range(length):
        element = int(input())
        list.append(element)
    print ("This is the list we use.")
    return list

def calculate_characteristic_vector_containing_all_possible_combinations_of_sums_of_elements_used_for_defining_2_substrings ():

    list_of_elements = []
    list_of_elements = reading_a_list_of_elements()

    characteristic_vector = []

    length_list = len (list_of_elements)

    maximum_sum_of_elements = 0

    for i in range(length_list):
        maximum_sum_of_elements += list_of_elements[i]

    for i in range (maximum_sum_of_elements+1):
        characteristic_vector.append (0)

    for i in range (length_list):

        for j in range (maximum_sum_of_elements, 0, -1):
            if characteristic_vector[j] != 0 and characteristic_vector[j+list_of_elements[i]] == 0:
                temporary_sum = j + list_of_elements [i]
                characteristic_vector [temporary_sum] = list_of_elements[i]

        if characteristic_vector[list_of_elements[i]] == 0:
            characteristic_vector[list_of_elements[i]] = list_of_elements[i]
    
    minimum_difference_of_the_sums = maximum_sum_of_elements+1
    first_sum_of_subsets = 0
    second_sum_of_subsets = 0

    for i in range (maximum_sum_of_elements, 0, -1):

        if characteristic_vector[i] != 0:
            j = maximum_sum_of_elements - i

            if abs(i - j) >= minimum_difference_of_the_sums:   
                break

            if abs(i - j) < minimum_difference_of_the_sums :
                first_sum_of_subsets = i
                second_sum_of_subsets = j
                minimum_difference_of_the_sums = (i - j)


    printing_a_solution_of_the_minimal_difference (first_sum_of_subsets, second_sum_of_subsets, characteristic_vector, list_of_elements)

def printing_a_solution_of_the_minimal_difference (first_sum_of_subsets, second_sum_of_subsets, characteristic_vector, list_of_elements):

    while first_sum_of_subsets != 0:
        print (characteristic_vector[first_sum_of_subsets])
        for i in range (len(list_of_elements)):
            if list_of_elements[i] == characteristic_vector[first_sum_of_subsets]:
                list_of_elements[i] = -1
        first_sum_of_subsets -= characteristic_vector[first_sum_of_subsets] 
    print ("The first subset. ")

    for i in range (len(list_of_elements)):
        if list_of_elements[i] != -1:
            print (list_of_elements[i])

    print ("The second subset.")

calculate_characteristic_vector_containing_all_possible_combinations_of_sums_of_elements_used_for_defining_2_substrings()