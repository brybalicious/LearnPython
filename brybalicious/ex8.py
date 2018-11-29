# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", 'two', "three", 'four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
#What is the above? I thought python relied on indentation for order?

#'But it didn't sing' comes out in double quotes in the output because it contains a single apostrophe in didn't... 
