#cocktail sort and gnome sort complexity
import random
import timeit
from decimal import Decimal
def start_console_application ():

    points_list = []
    sort_list = []
    while True:
        print ("1. Generate a list of n random natural numbers.")
        print ("2. Sort the list using the first algorithm.")
        print ("3. Sort the list using the second algorithm.")
        print ("4. See the worst case.")
        print ("5. See the average case.")
        print ("6. See the best case.")
        print ("0. Exit the program.")
    
        choice = input ("> ")

        if choice == "1":
            points_list = generate_points ()
            print (points_list)
        elif choice == "2":
            points_list = cocktail_sort (points_list)
        elif choice == "3":
            points_list = gnome_sort (points_list)
        elif choice == "4":
            print ("For which algorithm would you like to see the worst case?")
            print ("1. Cocktail sort.")
            print ("2. Gnome sort.")
            case_choice = input (">")
            length = int (input ("Length of the first list: "))
            if case_choice == "1":
                average_time_of_sorting = 0
                for i in range (5):
                    sort_list = worst_case_list_generator (length)
                    execution_time = timer_cocktail_sort (sort_list)
                    average_time_of_sorting = average_time_of_sorting + execution_time
                    print ("The length of the list is " + str(length))
                    print ("The execution time is " + str(execution_time))
                    length *= 2
                    sort_list = []

                average_time_of_sorting = average_time_of_sorting / 5
                print (" ---> The average timing of the worst case for Cocktail Sort is " + str(average_time_of_sorting))


            elif case_choice == "2":
                average_time_of_sorting = 0
                for i in range (5):
                    sort_list = worst_case_list_generator (length)
                    execution_time = timer_gnome_sort (sort_list)
                    average_time_of_sorting = average_time_of_sorting + execution_time
                    print ("The length of the list is " + str(length))
                    print ("The execution time is " + str(execution_time))
                    length *= 2
                    sort_list = []

                average_time_of_sorting = average_time_of_sorting / 5
                print (" ---> The average timing of the worst case for Gnome Sort is " + str(average_time_of_sorting))

            
        elif choice == "5":
            print ("For which algorithm would you like to see the average case?")
            print ("1. Cocktail sort.")
            print ("2. Gnome sort.")
            case_choice = input (">")
            length = int(input ("Length of the first list: "))
            if case_choice == "1":
                average_time_of_sorting = 0
                for i in range (5):
                    sort_list = generate_points (length)
                    execution_time = timer_cocktail_sort (sort_list)
                    average_time_of_sorting = average_time_of_sorting + execution_time
                    print ("The length of the list is " + str(length))
                    print ("The execution time is " + str(execution_time))
                    length *= 2
                    sort_list = []

                average_time_of_sorting = average_time_of_sorting / 5
                print (" ---> The average timing of the average case for Cocktail Sort is " + str(average_time_of_sorting))

            elif case_choice == "2":
                average_time_of_sorting = 0
                for i in range (5):
                    sort_list = generate_points (length)
                    execution_time = timer_gnome_sort (sort_list)
                    average_time_of_sorting = average_time_of_sorting + execution_time
                    print ("The length of the list is " + str(length))
                    print ("The execution time is " + str(execution_time))
                    length *= 2
                    sort_list = []

                average_time_of_sorting = average_time_of_sorting / 5
                print (" ---> The average timing of the average case for Gnome Sort is " + str(average_time_of_sorting))


        elif choice == "6":
            print ("For which algorithm would you like to see the best case?")
            print ("1. Cocktail sort.")
            print ("2. Gnome sort.")
            case_choice = input (">")
            length = int (input ("Length of the first list: "))
            if case_choice == "1":
                average_time_of_sorting = 0
                for i in range (5):
                    sort_list = best_case_list_generator (length)
                    execution_time = timer_cocktail_sort (sort_list)
                    average_time_of_sorting = average_time_of_sorting + execution_time
                    print ("The length of the list is " + str(length))
                    print ("The execution time is " + str(execution_time))
                    length *= 2
                    sort_list = []

                average_time_of_sorting = average_time_of_sorting / 5
                print (" ---> The average timing of the best case for Cocktail Sort is " + str(average_time_of_sorting))
                    
            elif case_choice == "2":
                average_time_of_sorting = 0
                for i in range (5):
                    sort_list = best_case_list_generator (length)
                    execution_time = timer_gnome_sort (sort_list)
                    average_time_of_sorting = average_time_of_sorting + execution_time
                    print ("The length of the list is: " + str(length))
                    print ("The execution time is: " + str(execution_time))
                    length *= 2
                    sort_list = []

                average_time_of_sorting = average_time_of_sorting / 5
                print (" ---> The average timing of the best case for Gnome Sort is " + str(average_time_of_sorting))

        elif choice == "0":
            print ("Goodbye :(.")
            return
        else: print ("Bad command :(.")

def generate_points(number_of_points):

    randomly_generated_points = []
    for i in range (0, number_of_points):
        random_point = random.randint(0,500)
        randomly_generated_points.append (random_point)

    return randomly_generated_points


def cocktail_sort(list): # best case = O(n), worst and average case = O(n^2)

    list_sorted = False

    length_list = len(list)
    start = 0
    end = length_list - 1

    while list_sorted == False:

        list_sorted = True
        for i in range (start, end):
            if (list[i] > list[i+1]):
                list[i], list[i+1] = list[i+1], list[i]
                list_sorted = False
        
        end = end - 1

        for j in range (end, start, -1):
            if (list[j] < list[j-1]):
                list[j], list[j-1] = list[j-1], list[j]
                list_sorted = False

        start = start + 1

        if (list_sorted == True):
            break

   # print (list, "  <- sorted list")

    return list


def gnome_sort(list): # best case = O(n), worst and average case = O(n^2)

    index = 0
    length_list = len(list)
    while index < length_list:

        if index == 0:
            index += 1
        if list[index]>=list[index-1]:
            index +=1
        else:
            list[index], list[index-1] = list[index-1], list[index]
            index = index-1

    #print (list, "<- sorted list")
    return list            

def best_case_list_generator(length):
    list = []
    for i in range(length):
        list.append(i+1)
    return list

def worst_case_list_generator(length):
    list = []
    for i in range (length):
        list.append (length-i)
    return list

def timer_cocktail_sort (list):
    start_of_timer = timeit.default_timer()
    cocktail_sort(list)
    end_of_timer = timeit.default_timer()
    timer = Decimal(float ("%.4f" % (end_of_timer - start_of_timer)))
    return timer

def timer_gnome_sort (list):
    start_of_timer = timeit.default_timer()
    gnome_sort(list)
    end_of_timer = timeit.default_timer()
    timer = Decimal(float ("%.4f" % (end_of_timer - start_of_timer)))
    return timer

start_console_application ()
