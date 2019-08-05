# Exercise 10
# tabby_cat = "\t\t\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."
#
# fat_cat = ("""I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """)

# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

#
# Escape What it does.
# \\ Backslash (\)
# \' Single- quote (')
# \" Double- quote (")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only)
# \r ASCII carriage return (CR)
# \t ASCII horizontal tab (TAB)
# \uxxxx Character with 16- bit hex value xxxx (Unicode only)
# \Uxxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)
# \v ASCII vertical tab (VT)
# \ooo Character with octal value oo
# \xhh Character with hex value hh


# Exercise 11
#
# # print("How old are you?",)
# # age = input()
# age = input("How old are you?")
#
# # print("How tall are you?",)
# # height = input()
# height = input("How tall are you?")
#
# # print("How much do you weigh?",)
# # weight = input()
#
# weight = input("How much do you weigh?")
#
# print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))
#
# # Exercise 12
# age = raw_input("How old are you? ")
# height = raw_input("How tall are you? ")
# weight = raw_input("How much do you weigh? ")
#
# print "So, you're %r old, %r tall and %r heavy." % (
# age, height, weight)

# Exercise 13

from sys import argv

script, first, second, third = argv
print(argv)
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
