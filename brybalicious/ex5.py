# -*- coding: utf-8 -*-

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Inches to cm and lbs to kgs:
intocm = 2.54
lbtokg = 1/2.2

print "Let's talk about %s." % name
print "He's %d %s tall." % (height * intocm, 'centimetres')
# Note, these operations on the height and weight have to be inside the parentheses, or you'll get an error.
# print intocm, lbtokg
print "He's %d %s heavy." % (weight * lbtokg, 'kgs')
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
# Note there are different format characters in python => %s, %d...
# https://docs.python.org/2.4/lib/typesseq-strings.html
# there's also a %r which is very useful.
#http://stackoverflow.com/questions/6005159/when-to-use-r-instead-of-s-in-python
# The %s specifier converts the object using str(), and %r converts it using repr().
# For some objects such as integers, they yield the same result, but repr() is special in that (for types where this is possible) it conventionally returns a result that is valid Python syntax, which could be used to unambiguously recreate the object it represents.
# Here's an example, using a date:
# >>> import datetime
# >>> d = datetime.date.today()
# >>> str(d)
# '2011-05-14'
# >>> repr(d)
# 'datetime.date(2011, 5, 14)'
# Types for which repr() doesn't produce Python syntax include those that point to external resources such as a file, which you can't guarantee to recreate in a different context.


# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height * intocm, weight * lbtokg, age + height*intocm + weight*lbtokg)
# interesting - you can specify variables in parentheses, but also perform operations on them there...
# Also if you use %r for the last substitution in this print(), you realise that the math is being done in float. Useful for debugging.

#Last bug - what do we have to do to make the math work out? Something to do with rounding or flooring floats. Now, what to do? Interestingly, the %d is doing some function on the math at the point where the calculated number is being substituted in. Is this .floor()?
