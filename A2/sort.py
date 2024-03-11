#cocktail sort and gnome sort
import random

def start_console_application ():

    points_list = []
    while True:
        print ("1. Generate a list of n random natural numbers.")
        print ("2. Sort the list using the first algorithm.")
        print ("3. Sort the list using the second algorithm.")
        print ("4. Exit the program.")
    
        choice = input (">")

        if choice == "1":
            points_list = generate_points ()
        elif choice == "2":
            step = int (input ("What value is the variable step? "))
            points_list = cocktail_sort (points_list, step)
        elif choice == "3":
            step = int (input ("What value is the variable step? "))
            points_list = gnome_sort (points_list, step)
        elif choice == "4":
            print ("Goodbye :(.")
            return
        else: print ("Bad command :(.")

def generate_points():

    number_of_points = int (input ("How many points would you like to generate? "))
    randomly_generated_points = []
    for i in range (0, number_of_points):
        random_point = random.randint(0,100)
        randomly_generated_points.append (random_point)

    print (randomly_generated_points)
    return randomly_generated_points


def cocktail_sort(list, step):

    number_of_steps_done_during_sorting = 0
    list_sorted = False

    length_list = len(list)
    start = 0
    end = length_list - 1

    while list_sorted == False:

        list_sorted = True
        for i in range (start, end):
            if (list[i] > list[i+1]):
                list[i], list[i+1] = list[i+1], list[i]
                number_of_steps_done_during_sorting += 1
                list_sorted = False

                if (number_of_steps_done_during_sorting % step == 0):
                    print (list)
        
        end = end - 1

        for j in range (end, start, -1):
            if (list[j] < list[j-1]):
                list[j], list[j-1] = list[j-1], list[j]
                number_of_steps_done_during_sorting += 1
                list_sorted = False

                if (number_of_steps_done_during_sorting % step == 0):
                        print (list)

        start = start + 1

        if (list_sorted == True):
            break

    print (list, "  <- sorted list")

    return list


def gnome_sort(list, step):

    number_of_steps_done_during_sorting = 0
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
            number_of_steps_done_during_sorting += 1
            if (number_of_steps_done_during_sorting % step == 0):
                print (list)

    print (list, "<- sorted list")
    return list            

start_console_application ()