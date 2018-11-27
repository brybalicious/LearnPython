# -*- coding: utf-8 -*-

# This line imports the argv module from the sys package
# which makes the argv actions available in this script
#  Interestingly, if you run a script without importing argv, yet you type 
#  in args when you run the script in shell (!= python interpreter), it 
#  still runs and just ignores the args...
from sys import argv

# Here we unpack argv and store them in variables
script, filename = argv

# Here we open a file which we're passed as an argv, but don't do anything
# with it yet besides storing the open file in a file object variable 'txt'
# The contents of the file aren't returned here...
txt = open(filename)

# The following block is good practice, so that any opened file is always closed in the end, regardless of what happens in between...
#>>> with open('workfile', 'r') as f:
#...     read_data = f.read()
#>>> f.closed
#True

# Just telling you what the file is, to show how argv works
print "Here's your file %r:" % filename
# Here's the magic.. we read the file we've opened, and display it
print txt.read()

# This bit's just a useless way of showing you can take a filename from
# raw_input... and store that name in the file_again variable, then open
# a file object by passing the filename, and storing the open file object
# in txt_again
print "Type the filename again:"
file_again = raw_input("> \a")
txt_again = open(file_again)

# And then print the contents to shell in the same way - using read()
# On the opened file object...
print txt_again.read()

# Here we will close the file instances we have opened and stored in 'txt' and 'txt_again' file object variables
txt.close()
txt_again.close()

#The following prints a confirmation of whether the objects have been closed...
print "Is txt closed?:", txt.closed
print "Is txt_again closed?:", txt_again.closed

# The sample exercise wants you to type 'python' into shell to open the python interpreter
# Then, you're supposed to type the following at the prompt - note the '':
#>>> open('ex15_sample.txt').read()
# Then you should expect this output:
#"This is stuff I like to write.\nComes out when called up by a python script.\nA'ight!"

#The mistake I was making is that I was trying to open the python script ex15.py inside the interpreter... that requires something like
#>>> execfile('ex15.py')
#I guess we'll soon see, but that would be what you'd call to execute a script from inside another script, right?
#Pay attention to where you need to pass filenames as strings (bounded by '') and where you don't. I couldn't figure out how to pass the argv elements to execfile, but maybe because I was a n00b trying to pass them to open()