# Exercise 23
import Exercise25

# sentence = "All good things come to those who wait."
# # word = Exercise25.break_words(sentence)
# # print(word)
#
# print(Exercise25.sort_words(sentence))
# # print(word)
# test = [1234, 123]
# print(Exercise25.print_first_word(test))
# print(Exercise25.print_last_word(test))


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
        \tThe lovely world
        with logic so firmly planted
        cannot discern \n the needs of love
        nor comprehend passion from intuition
        and requires an explantion
        \n\t\twhere there is none.
        """


print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont))


sentence = "All god\tthings come to those who weight."

words = Exercise25.break_words(sentence)
sorted_words = Exercise25.sort_words(words)

Exercise25.print_first_word(words)
Exercise25.print_last_word(words)
Exercise25.print_first_word(sorted_words)
Exercise25.print_last_word(sorted_words)
sorted_words = Exercise25.sort_sentence(sentence)
print(sorted_words)

Exercise25.print_first_and_last(sentence)
Exercise25.print_first_and_last_sorted(sentence)

