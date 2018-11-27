from sys import argv

# argv is a module/library which stands for 'Argument Variable'
# This is the variable that holds your arguments which you pass
# to the python script (.py file) when you run it.

script, first, second, third = argv

# The above line 'unpacks' argv into a bunch of separate variables. Not 
# sure of the syntax - was argv a dict[]?

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
fourth = raw_input("Oh and I forgot - you should input a fourth argument: ")
print "Your arguments are: %s, %s, %s, %s" % (first, second, third, fourth)

# Note, the command line arguments come in as strings. You can cast them..