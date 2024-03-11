import random

def choosing_the_backtracking_method():
    print ("1. Choose the iterative method for solving the problem using backtracking.")
    print ("2. Choose the recursive method for solving the problem using backtracking.")

    choice = input(">")

    if choice == "1":
        determine_all_possbile_ways_of_adding_operators_between_numbers_iterative()
    elif choice == "2":
        determine_all_possbile_ways_of_adding_operators_between_numbers_recursive()
    else: return

def generate_random_array (length_array):

    array = []
    for i in range (length_array):
        array.append(random.randint(0,100))
    return array


def calculate_the_result_after_adding_operators_between_numbers (numbers_for_the_expression, stack_used_for_determining_all_combinations):

    result_of_expression = numbers_for_the_expression[0]
    for i in range (1,len(numbers_for_the_expression)):
        if stack_used_for_determining_all_combinations[i-1]==1:
            result_of_expression-=numbers_for_the_expression[i]
        else:
            result_of_expression+=numbers_for_the_expression[i]
    if result_of_expression <0:
        return False
    return True
    
def print_the_expression_after_adding_the_operators (numbers_for_the_expression, length_array, stack_used_for_determining_all_combinations):

    printing_array = []
    printing_array.append(numbers_for_the_expression[0])
    for i in range (1,length_array):
        if stack_used_for_determining_all_combinations [i-1] == 1:
            printing_array.append ("-")
            printing_array.append (numbers_for_the_expression[i])
        else: 
            printing_array.append ("+")
            printing_array.append (numbers_for_the_expression[i])

    print (printing_array)
        

def determine_all_possbile_ways_of_adding_operators_between_numbers_iterative ():

    numbers_for_the_expression = []
    length_array = int(input ("What length is the array? "))
    numbers_for_the_expression = generate_random_array(length_array)
    print(numbers_for_the_expression) 

    stack_used_for_determining_all_combinations = [-1]
    number_of_elements_existing_on_the_stack = 0
    while number_of_elements_existing_on_the_stack != -1:
        if stack_used_for_determining_all_combinations[number_of_elements_existing_on_the_stack] <1:
            stack_used_for_determining_all_combinations[number_of_elements_existing_on_the_stack] +=1
            if  len(stack_used_for_determining_all_combinations)==length_array-1:
                if calculate_the_result_after_adding_operators_between_numbers (numbers_for_the_expression, stack_used_for_determining_all_combinations):
                    print_the_expression_after_adding_the_operators(numbers_for_the_expression, length_array, stack_used_for_determining_all_combinations)

            else:
                stack_used_for_determining_all_combinations.append (-1)
                number_of_elements_existing_on_the_stack+=1
        else:
            number_of_elements_existing_on_the_stack-=1
            stack_used_for_determining_all_combinations.pop()

def determine_all_possbile_ways_of_adding_operators_between_numbers_recursive ():
    
    numbers_for_the_expression = []
    length_array = int(input ("What length is the array? "))
    numbers_for_the_expression = generate_random_array(length_array)
    print(numbers_for_the_expression) 
    stack_used_for_determining_all_combinations = [-1]
    number_of_elements_existing_on_the_stack = 0
    generating_the_solutions_recursive (numbers_for_the_expression, length_array, number_of_elements_existing_on_the_stack, stack_used_for_determining_all_combinations)

def generating_the_solutions_recursive(numbers_for_the_expression, length_array, number_of_elements_existing_on_the_stack, stack_used_for_determining_all_combinations):

    for i in range (0, 2):
        stack_used_for_determining_all_combinations[number_of_elements_existing_on_the_stack] = i
        if len(stack_used_for_determining_all_combinations)==length_array-1:
            if calculate_the_result_after_adding_operators_between_numbers (numbers_for_the_expression, stack_used_for_determining_all_combinations):
                print_the_expression_after_adding_the_operators(numbers_for_the_expression, length_array, stack_used_for_determining_all_combinations)
        if number_of_elements_existing_on_the_stack < length_array-1:
            stack_used_for_determining_all_combinations.append (-1)
            generating_the_solutions_recursive (numbers_for_the_expression, length_array, number_of_elements_existing_on_the_stack+1, stack_used_for_determining_all_combinations)
            stack_used_for_determining_all_combinations.pop()


choosing_the_backtracking_method ()
