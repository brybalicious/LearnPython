print "I shall now count my chickens:"

#Seems that ',' is a concatenator. Somehow in the output, it knows to put a space between the end of 'Hens' and the start of the numerical output. I'll try not putting a space after the comma and see what happens.
print "Hens",25 + 30 / 6
#apparently it still appends the space. Perhaps comma always does that.


#% is modulus (remainder). Remember bodmas. Well actually it's "PEMDAS = Parentheses, Exponents, Multiplication, Division, Addition, Subtraction"
#I guess modulus happens after multiplication but before subtraction
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

#There is a hidden math error here, because the 1/4 is not calculated to a floating point number. In order to do this, simply specify sig figs with a decimal point.
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4.0 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5-7
print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >=-2
print "Is it less or equal?", 5<=-2
