# number = input("please enter a number")
# a=[]
# listRange = list(range(1,number+1))
#
# for number1 in listRange:
#     if number%number1 == 0:
#         a.append(number1)
#
# print (a)
#Another solution


num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)




