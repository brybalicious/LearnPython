# -*- coding: utf8 -*-

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\a \\a ASCII Bell -->OMG MAKES A BELL SOUND!!!
Backspace\bDon't know what this does...
\f Formfeed
\r ASCII Carriage Return
\t ASCII Horizontal Tab
\vVertical Tab"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/", "-", "\\", "|"]:
		print "%s\r" % i,

#Note, if you printed %r here, you would get something different. %s is what you want to see displayed. %r is for debugging
# Why does this keep printing over the same character space, rather than printing
# a huge long line?