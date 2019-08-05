# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven
# # "_" is an underscore character
# _ = 22
#
# print(_)
#
# print("Hey %s   there." % "you")
# print("hey  %s r  "  % "adarsh")
# print("There are", cars, "cars available.")
# print("There are only", drivers, "drivers available.")
# print("There will be", cars_not_driven, "empty cars today.")
# print("We can transport "+"{:.2f}".format(carpool_capacity) + " people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", average_passengers_per_car, "in each car.")


#More examples 

# my_name = 'Zed A. Shaw'
# my_age = 35 # not a lie
# my_height = 74 # inches
# my_weight = 180 # lbs
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'
#
# print("Let's talk about %s." % my_name)
# print("He's %d inches tall." % my_height)
# print("He's %d pounds heavy." % my_weight)
# print("Actually that's not too heavy.")
# print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
# print("His teeth are usually %s depending on the coffee." % my_teeth)
#
# # this line is tricky, try to get it exactly right
# print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

# Study drill
var_name = 'Zed A. Shaw'
var_age = 35  # not a lie
var_height = 74  # inches
var_weight = 180  # lbs
var_eyes = 'Blue'
var_teeth = 'White'
var_hair = 'Brown'

print("Let's talk about %s." % var_name)
print("He's %d inches tall." % var_height)
print("He's %d pounds heavy." % var_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (var_eyes, var_hair))
print("His teeth are usually %s depending on the coffee." % var_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (var_age, var_height, var_weight, var_age + var_height + var_weight))

# Try to write some variables that convert the inches and pounds to centimeters and kilos.
# Do not just type in the measurements. Work out the math in Python.

print(round(1.234566, 5))
