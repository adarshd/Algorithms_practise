# # Exercise 15
# from sys import argv
#
# script, filename = argv
#
# txt = open(filename)
#
# print("Here's your file %r:" % filename)
# print(txt.read())
#
# print("Type the filename again:")
# file_again = input("> ")
#
# txt_again = open(file_again)
#
# print(txt_again.read())

from sys import argv

script, filename = argv

txt = open(filename)
print(txt.read())
file_again = input(">")
file_again = open(file_again)
print(file_again.read())


