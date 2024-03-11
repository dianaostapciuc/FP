""" 
    Given the set of positive integers S, partition this set into two subsets S1 and S2
    so that the difference between the sum of the elements in S1 and S2 is minimal.
    For example, for set S = { 1, 2, 3, 4, 5 }, the two subsets could be S1 = { 1, 2, 4 }
    and S2 = { 3, 5 }. Display at least one of the solutions.

"""
def creating_the_list_of_elements ():

    list = []
    length = int(input ("What's the length of your list? "))
    for i in range(length):
        element = int(input())
        list.append(element)
    print ("This is the list we use.")
    return list

def paritioning_the_list_of_elements_into_2_subsets_with_the_naive_method ():

    list_of_elements = []
    list_of_elements = creating_the_list_of_elements()

    length_list = len(list_of_elements)

    total_sum_of_elements = 0
    for i in range(length_list):
        total_sum_of_elements += list_of_elements[i]

    minimum_difference_of_sums = total_sum_of_elements

    stacking_all_possible_combinations_of_elements = [-1]
    number_of_elements_existing_on_the_stack = 0
    while number_of_elements_existing_on_the_stack != -1:
        if stacking_all_possible_combinations_of_elements[number_of_elements_existing_on_the_stack] <1:
            stacking_all_possible_combinations_of_elements[number_of_elements_existing_on_the_stack] +=1
            if  len(stacking_all_possible_combinations_of_elements)==length_list:
                temporary_minimum = calculating_the_difference_of_the_sums(list_of_elements, stacking_all_possible_combinations_of_elements)
                if temporary_minimum < minimum_difference_of_sums:
                    minimum_difference_of_sums = temporary_minimum
            else:
                stacking_all_possible_combinations_of_elements.append (-1)
                number_of_elements_existing_on_the_stack+=1
        else:
            number_of_elements_existing_on_the_stack-=1
            stacking_all_possible_combinations_of_elements.pop()

    stacking_all_possible_combinations_of_elements = [-1]
    number_of_elements_existing_on_the_stack = 0
    while number_of_elements_existing_on_the_stack != -1:
        if stacking_all_possible_combinations_of_elements[number_of_elements_existing_on_the_stack] <1:
            stacking_all_possible_combinations_of_elements[number_of_elements_existing_on_the_stack] +=1
            if  len(stacking_all_possible_combinations_of_elements)==length_list:
                temporary_minimum = calculating_the_difference_of_the_sums(list_of_elements, stacking_all_possible_combinations_of_elements)
                if temporary_minimum == minimum_difference_of_sums:
                    print_solution (list_of_elements, stacking_all_possible_combinations_of_elements)
                    break
            else:
                stacking_all_possible_combinations_of_elements.append (-1)
                number_of_elements_existing_on_the_stack+=1
        else:
            number_of_elements_existing_on_the_stack-=1
            stacking_all_possible_combinations_of_elements.pop()

def print_solution (list_of_elements, stack):
    
    for i in range (len(list_of_elements)):
        if stack [i] == 1:
            print (list_of_elements[i])

    print ("This is the first subset.")

    for i in range (len(list_of_elements)):
        if stack [i] == 0:
            print (list_of_elements[i])

    print ("This is the second subset.")

 
def calculating_the_difference_of_the_sums (list_of_elements, stack):
    
    sum_of_first_subset = 0
    sum_of_second_subset = 0
    for i in range (len(stack)):
        if stack[i] == 1:
            sum_of_first_subset += list_of_elements[i]
        else: sum_of_second_subset += list_of_elements[i]
    difference_of_sums = abs(sum_of_first_subset-sum_of_second_subset)
    return difference_of_sums

paritioning_the_list_of_elements_into_2_subsets_with_the_naive_method ()
