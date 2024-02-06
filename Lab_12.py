import time
import random
'''
# Author Brahma Dathan
# This program does a comparison of the running times for sequential and binary
# search algorithms.

# This function computes the running time for sequential search; the list
# my_list and the
# number of iterations are passed as parameters. The program repeats the
# search number_of_tirlals times.
# It returns the average time for one trial.

# Convert the pseudo code to Python code


def sequential_search(my_list, number_of_trials):
    # Observe indentation in the pseudo code
    # store the length of my_list in length
    # if the length of my_list is 0, return  -1
    # get the current time into a variable named time1 (see binary search code)
    # repeat number_of_trials times
    #        let count = iteration number
    #        if count % length is 0
    #           set target to 1+ the content at the last cell of my_list
    #        otherwise
    #           set target to the location at my_list[count % length]
    #        set index to 0
    #        while index is less than length and cell at index is not
    #                    equal to target
    #           increment index
    # get the current time into a variable named time2 (see binary search code)
    # return the average time for a single iteration using the
    # difference of time2, time1, and number_of_trials
# This function computes the running time for binary search; the list my_list
# and the
# number of iterations are passed as parameters. The program repeats the search
# number_of_trials times.
# It returns the average time for one trial.
'''

def sequential_search (my_list, number_of_trials):
    length = len (my_list)
    if length == 0:
        return -1 
    time1 = time.perf_counter()
    for count in range (number_of_trials):
        if count % length == 0:
            target = my_list [-1] + 1 
        else:
            target = my_list [count % length]
        index = 0 
        while (index < length): #and (my_list [index] != target):
            index += 1
    time2 = time.perf_counter()
    return (time2 - time1) / number_of_trials

def binary_search(my_list, number_of_trials):
    length = len(my_list)
    if length == 0:
        return -1
    time1 = time.perf_counter()
    for count in range(number_of_trials):
        if count % length == 0:
            target = my_list[-1] + 1
        else:
            target = my_list[count % length]
        low = 0
        high = len(my_list) - 1
        while low <= high:
                mid = (low + high) // 2
                if my_list[mid] == target:
                    break
                elif my_list[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
    time2 = time.perf_counter()
    return (time2 - time1) / number_of_trials

# Sets up the experiment by creating the lists and calling the two search
# functions.

def experiment():
    start_list_size = int(input("Enter start list size: "))
    end_list_size = int(input("Enter end list size: "))
    increment = int(input("Enter list size increment: "))
    seq_number_of_trials = int(input("Enter number of iterations for sequential search: "))
    bin_number_of_trials = int(input("Enter number of iterations for binary search: "))
    for list_size in range(start_list_size, end_list_size + 1, increment):
        my_list = []    
        low = 0
        high = 10
        for index in range(list_size):
            my_list.append(random.randint(low, high))
            low = high + 1
            high = high + 10
        seq_search_time = sequential_search(my_list, seq_number_of_trials)
        bin_search_time = binary_search(my_list, bin_number_of_trials)
        print("List size:", list_size)
        print("                       Time for Sequential Search",
              format(seq_search_time, ".10f"))
        print("                       Time for Binary Search    ",            
              format(bin_search_time, ".10f"))
        
experiment()

