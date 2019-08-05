# x = "There are %d types of people." % 10  # variable
# binary = "binary"  # Variable
# do_not = "don't"
# y = "Those who know %s and those who %s." % (binary, do_not)
#
# print(x)
# print(y)
#
# print("I said: %r." % x)
# print("I also said: '%s'." % y)
#
#
# hilarious = True
# joke_evaluation = "Isn't that joke so funny?! %r"
#
# print(joke_evaluation % hilarious)
#
# w = "This is the left side of..."
# e = "a string with a right side."
#
# print(w)
# print(e)
# print(w + e)


# More Printing

#
# print("Mary had a little lamb.")
# print("Its fleece was white as %s." % 'snow')
# print("And everywhere that Mary went.")
# print("." * 10)  # what'd that do?
#
# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"
# #
# # # watch that comma at the end. try removing it to see what happens
# print(end1 + end2 + end3 + end4 + end5 + end6)
# print(end7 + end8 + end9 + end10 + end11 + end12)

# Exercise 8

formatter = "%r %r %r %r"

# print(formatter % (1, 2, 3, 4))
# print(formatter % ("one", "two", "three", "four"))
# print(formatter % (True, False, False, True))
# print(formatter % (formatter, formatter, formatter, formatter))
# print(formatter % (
#                    "I had this thing.",
#                    "That you could type up right.",
#                    "But it didn't sing.",
#                    "So I said goodnight."
#                    ))
# Exercise 9				  
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""There's something going on here.
         With the three double- quotes.
         We'll be able to type as much as we like.
         Even 4 lines if we want, or 5, or 6.""")



