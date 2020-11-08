"""
Week 10 HW: Profiling  03/19/19
Tests the timing of two sorting algorithms, bubble sort and selection sort, using cProfile

Here, I implemented two different sorting alorithms, Bubble Sort and Selection Sort. 
I used both algorithms to sort the same randomly generated list of numbers, then
checked the timing using cProfile.
Credit for bubble() and selection() go to George Seif:
https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
"""

import cProfile
import random

#Bubble sort of a list
def bubble(list):
    def swap(i, j):
        list[i], list[j] = list[j], list[i]

    n = len(list)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if list[i-1] > list[i]:
                swap(i-1, i)
                swapped = True

    return list

#Selection sort of a list
def selection(list):
    for i in range(len(list)):
        minimum = i

        for j in range(i+1, len(list)):
            if list[j] < list[minimum]:
                minimum = j

        list[minimum], list[i] = list[i], list[minimum]

    return list


# Generate a list of 1000 random integers in the range(0-100)
random_list = []
for _ in range(1000):
    value = random.randint(0, 100)
    random_list.append(value)

# Use cProfile to get the timing for bubble sort and selection sort of random_list
# selection() will be faster than bubble()
print("cProfile of bubble().....")
cProfile.run('bubble(random_list)')
print("cProfile of selection().....")
cProfile.run('selection(random_list)')

