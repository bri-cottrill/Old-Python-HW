
"""
02/13/19 Week 5 HW - Generators II.
Get user input for file to open, then pass to wrap_filetext()

Assignment Prompt:
Rewrap text from the filename passed so that it fits an 80 column window without breaking any words. 
Use a generator that yields the next line of text, containing as many words as possible.
"""

import textwrap

def wrap_filetext(filename):
    """Yield the wrapped line of the file. Max 80 characters per line."""
    try:
        open_file = open(filename)
    except:
        print("File cannot be opened: ", filename)
        print("Goodbye.")
        exit()
    wrapper = textwrap.TextWrapper(width=80)
    yield from (wrapper.fill(text=' '.join(line.split(" "))) for line in open_file)

entered_file = input("Enter the file name you want to wrap: ")
for wrap_line in wrap_filetext(entered_file):
    print(wrap_line)

