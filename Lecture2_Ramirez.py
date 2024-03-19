# 

# int(56)

# print((float(54))) #convert int to float

# print(9.conjugate(8))
# x=5
# y=5

# print(y % x)

# y = pow(6,2)

# print("QUOTIENT:", y)

quotient, remainder = divmod(8,7)
# True division= floating ang result
# FLoor division=int ang result, round down
# x=14
# y=2

# print("Sum of of X and Y: ", x + y) #addition
# print("Difference of X and Y: ", x - y) #subtraction
# print(x * y)
# print(x / y)
# print(x // y)
# print(x ** y)
# print(x // y)
# print(abs(y))
# print(float(y))
# print(complex(y))
# print(divmod(x // y))

# # #LIST
# # dog = ("golden retriever", "husky", "aspin", "poodle")
# # print(dog(0))

# # type("hello world")
# # PART 1: Cloning Repository

# print('Kumusta World')
# character_annie = '0.9' # naming the characters of out story
# mother = 'Leni'

# # They went to the market
# sentence = character_annie + ' and ' + mother + ' went to the market.' 
# print(sentence)
# print(type(character_annie))

# Mga Bilihin ni Jo
# list_of_bilihin = ["carrots", "cabbage", "patatas"]
# print(list_of_bilihin[1])

# cabbages = 21
# patatas = 365
# # 1 nilaga = 2 cabbages and 3 patatas, how many nilaga can I make, and how many patatas left?
# nilaga = cabbages // 2
# number_of_patatas_left = patatas - nilaga*3

# print("Number of Nilaga:", nilaga)
# print("number of patatas left:", number_of_patatas_left)

# name = "121-12-13"
# letters = name.split('-')
# print(letters)

"""
Exercise 1 - Procedural Programming
Quinmar Q. Ramirez
2023-14871
BS Geodetic Engineering
"""

# dd = 118.42069

# # Getting degrees
# degree = int(dd)
# print("DEGREES:", degree)

# # Getting minutes
# minutes = (dd - degree) * 60
# minutes_fractional = int(minutes)
# print("MINUTES", minutes)

# # Getting seconds
# seconds = (minutes - minutes_fractional) * 60
# print("SECONDS", seconds)

# # The Degree-Minute-Second 
# DMS = str(degree)  +"-" + str(minutes_fractional) + "-" + str(round(seconds, 2))
# print("DMS: ", DMS)

# # Converting DMS to DD
# dms = "118-25-14.48"
# values = dms.split("-")
# print("Values:", values)

# # degrees = int(values[0])
# minutes = int(values[1])
# seconds = float(values[2])

# dd= degrees + (minutes/60) +(seconds/3600)

# # The Decimal Degree
# print("DD:", round(dd,6))

