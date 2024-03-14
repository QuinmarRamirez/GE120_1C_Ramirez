# # Lecture 3 Notes

# listahan = ["mafe", "justin", "mika"]
# # print(listahan[-3:3])

# # Tuples
# tuple_1 = ("maja", "gianna", "jewel")
# # print(tuple_1)

# # tuples are immutable
# # tuple_1[0] = "quinmar"

# # dictionaries
# dict = {
#     "name": "Bogart",
#     "age": "2",
#     "color": "white",
#     "favorite_num": 3.14,
#     1.113: 45
#     }

# # print(dog{1.113})
# # print(dog)

# grade = 91.9999

# if grade >= 92:
    # print("YAHOO")
# elif grade >= 60:
    # print("NICE")
# else: 
    # print("SAD")

# LOOPS AND BREAK CONTINUE AND PASS

# numbers = range(10)
# for number in numbers:
#     if number == 5:
#         pass

# rec = 0
# while rec <= 5000:
#     rec = int((input"enter REC:   "))
#     kulanag = 5000 - rec
#     if rec > 4500"
#         print("onti nalang naman kulang pwede na")
#         break

# print("kulang ka ng REC na", kulang)
# print("PASOK NA REC")
# print("-----END------")

# ASSIGNING AZIMUTH TO BEARING
    if azimuth > 0 and azimuth < 90:
        bearing = 'S {: ^10} W' .format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {: ^10} W' .format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = 'N {: ^10} E' .format(azimuth -180)
    elif azimuth > 270 and azimuth < 360:
        bearing = 'S {: ^10} E' .format(360 - azimuth)
    elif azimuth ==0:
        bearing = "DUE SOUTH"
    elif azimuth ==90:
        bearing = "DUE WEST"
    elif azimuth ==180:
        bearing = "DUE NORTH"
    elif azimuth ==270:
        bearing = "DUE EAST"
    else:
        bearing = "NOT APPLICABLE"

    line = (counter, distance, bearing)  # create tuple of the line
    lines.append(line)

    # Ask for input
    yn = input("DO YOU WANT TO ADD A NEW LINE? [yes/no]  ")
    if yn.lower() =="yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print ("\n\n")
print ('{: ^10} {: ^10} {: ^10}' .format ("LINE NO.", "DISTANCE", "BEARING"))
for line in lines:
     print ('{: ^10} {: ^10} {: ^10}' .format (line [0], line [1], line [2]))

print ("-----END-----")


