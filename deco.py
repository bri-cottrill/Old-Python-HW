"""
03/17/19 Week 9 HW - Decorators

Decorate print() such that (A) it refuses to print anything under ten characters long and 
(B) only five calls are allowed, and demonstrate these restrictions when the program is run.
"""

import functools

"""
Print the passed string (accessed in args[0]) if it is 10 or more characters long.
Only allow for a max of 5 function calls (through use of .num_calls).
"""
def print_deco(func):
    @functools.wraps(func)
    def wrapper_print_deco(*args, **kwargs):
        wrapper_print_deco.num_calls += 1
        if wrapper_print_deco.num_calls <= 5:
            if len(args[0]) >= 10:
                print(f"{args[0]}")
    wrapper_print_deco.num_calls = 0
    return wrapper_print_deco

@print_deco
def my_print(my_string):
    print(my_string)


# Demonstration of the decorator
print("Beginning tests of my_print and print_deco...")

my_print("This is call No. 1")  #Should print
my_print("No. 2")  #Should not print
my_print("Call number 3")  #Should print
my_print("Fourth call")  #Should print
my_print("#5: Last call") #Should print
my_print("Call number six")  #Should not print

print("All done! A look at the code will show that there were 6 function calls.")
