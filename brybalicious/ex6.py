# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Interestingly, joke_evaluation contains a string with a hanging format string
#which means you can use % on the joke_evaluation variable
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#In this case + is a string concatenator
print w + e
