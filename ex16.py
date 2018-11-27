from sys import argv

script, filename = argv

# https://docs.python.org/2/library/functions.html#open
# http://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w
print "You have passed a file... here are the contents..."
print "Opening the file..."
# See above docs about which parameter to use for open(...,'?')
target = 0

# something's going wrong below, when it comes to reading from target, and also, writing to target in particular.
# I learned that even the indentation of comments within a loop, affects the operation of the loop
# Also, I'm not sure about the scope of target outside the with context manager...

with(open(filename,'r+')) as target:
	print target.read()
	# target.close()

	print "We're going to erase %r" % filename
	print "If you don't want that, hit CTRL-C (^C)"
	print "Otherwise, hit RETURN"

	raw_input("?")

	#	print "Opening the file..."
	#	target = open(filename, 'w')

	# Don't need to truncate, because open(...,'w') truncates as it opens...
	# But if we open(...,'r+'), then we should truncate...
	print "Truncating the file. Goodbye!"
	#target.truncate()
	print target.read()
	print "Now I'm going to ask you for three lines."

	line1 = raw_input("Line 1: ")
	line2 = raw_input("Line 2: ")
	line3 = raw_input("Line 3: ")

	print "I'm going to write these to the file."

	print "%r\n%r\n%r\n" % (line1, line2, line3)
	target.write("%r\n%r\n%r\n" % (line1, line2, line3))
	
	print "The file now reads as follows:"
	#	target.close()
	#	target = open(filename,'r')
	print target.read()

	print "And finally, we close it."
	# Don't need this because we're simply ending the with...as... statement
	#	target.close()
	print "Is the file closed?",
	if(target.closed):
		print "YES"
	else:
		print "NO"