# -*- coding: utf-8 -*-

print "How old are you?",
#Note the comma ',' at the end of the print line ensures the input occurs at the same line that the prompt is on. If we leave out the comma, it moves to the next line.
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

# Why do we put the parentheses on the next line, and tab it in?
# Just for style - Python people like no more than 80 chars in a line.
# Seems it makes no real difference whether we tab..
# nor whether we put it on the next line!

#We could also code it like this:

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Don't use input() - there's a security vulnerability... If you need to take inputs as integers, simply cast as an int, e.g. x = int(raw_input())