Lecture 3


# # LISTS
# listahan = ["mafe", "justin", "mika", "uste"]
# print(listahan)

# # gusto si mika makuha (position)
# print(listahan[2])

# # subset of the list, mafe and si justin
# print(listahan[0:2])

# # print(listahan[1:3])

# # nagstastart sa simula
# print(listahan[:3])

# # start from index, end sa dulo
# print(listahan[2:])

# print(listahan[-1])
# print(listahan[-2])

# # gets first item, last item, then those in between
# print(listahan[-3:3])

# # Addition of Lists
# print(listahan[0:2]+listahan[2:4])
# print(listahan[0:4])

# listahan[0] = "chelzy"
# print(listahan)

# TUPLES
# tuple_1 = ("maja", "gianna", "jewel")
# print(tuple_1)

# # tuples are immutable
# tuple_1[0] = "quinmar"

# # print(tuple_1)

# # NESTED LISTS
# list_1 = [ ["apple", "bola", "carton"] , ["apricot", "banana", "cow"]  ]
# print(list_1[0][2])

# # NESTED TUPLES
# tuple_2 = ((12.1244, -12.12414),(35.46261,-67.1231),(123.124, 56.232))
# print(tuple_2[2][0])

# # DICTIONARIES - key value pairs
# dog = {
#         "name": "Bogart",
#         "age": 2,
#         "color": "white",
#         "favorite_num": 3.14,
#         1.113: 45  #pwede si number as key (float or int)
#        }

# # print(dog[1.113])
# # print(dog.values())  #returns a list of values
# # # print(dog.keys())  #returns a list of keys

# # dog["favorite_num"] = 39

# # print(dog["favorite_num"])


# # # LOOPS AND BREAK CONTINUE AND PASS

# # for number in range(10):
# #     if number == 5:
# #         pass

# rec = 0
# while rec <= 5000:
#     rec = int(input("enter REC: "))
#     kulang = 5000 - rec
#     if rec >= 4500:
#         pass
#         print("onti nalang kulang, kaya mo yan")
#     print("kulang ka ng REC na", kulang)

# print("PASOK NA REC")
# print("-------END-----")



from prettytable import PrettyTable

# Initializing Variables
counter = 1
lines = []

# Create a Sentinel-Controlled Loop
while True:
    print()
    print("LINE NO. ", counter)
     
    # Input Distance
    invalid_syntax = True  
    while invalid_syntax:
        distance = input("ENTER DISTANCE: ")
        try:
           distance = float(distance)
           if distance < 0:  # Check if the input is negative
               print("Distance must be a positive number.")
           else:
               invalid_syntax = False  # Valid input, exit the loop
        except ValueError:
               print("Invalid Syntax. Distance must be a number.")

    # Input Azimuth
    azimuth = float(input("ENTER AZIMUTH FROM THE SOUTH (in decimal degrees): ")) # 92.44

# Converting Decimal Degrees to Degrees-Minutes-Seconds

# Assigning Azimuth to Bearing

    if azimuth > 0 and azimuth < 90:
        dms_bearing = 'S {: ^10} W' .format(dms_azimuth)

    elif azimuth > 90 and azimuth < 180: #92.44
        bearing = 180 - azimuth #87.44
        degrees_1 = int(bearing)  #87
        int_azimuth = int(azimuth) #92
        remainder_minutes_1 = (azimuth - int_azimuth) * 60  # 26
        minutes_1 = int(remainder_minutes_1)
        remainder_seconds_1 = (remainder_minutes_1 - minutes_1) * 60 
        seconds_1 = round(remainder_seconds_1, 2) 
        dms_bearing = "N    {}-{}-{:.2f}    W".format(degrees_1, minutes_1, seconds_1)
        

    elif azimuth > 180 and azimuth < 270:
        bearing = azimuth - 180
        degrees_2 = int(bearing)  
        int_azimuth = int(azimuth)
        remainder_minutes_2 = (azimuth - int_azimuth) * 60   
        minutes_2 = int(remainder_minutes_1)
        remainder_seconds_2 = (remainder_minutes_2 - minutes_2) * 60 
        seconds_2 = round(remainder_seconds_2, 2) 
        dms_bearing = "N    {}-{}-{:.2f}    W".format(degrees_2, minutes_2, seconds_2)
    

    elif azimuth > 270 and azimuth < 360:
        bearing = 360-azimuth
        degrees_3 = int(bearing)  
        int_azimuth = int(azimuth)
        remainder_minutes_3 = (azimuth - int_azimuth) * 60  # 
        minutes_3 = int(remainder_minutes_3)
        remainder_seconds_3 = (remainder_minutes_3 - minutes_3) * 60 
        seconds_3 = round(remainder_seconds_3, 2) 
        dms_bearing = "N    {}-{}-{:.2f}    W".format(degrees_3, minutes_3, seconds_3)
   
    elif azimuth ==0:
        dms_bearing = "DUE SOUTH"

    elif azimuth ==90:
        dms_bearing = "DUE WEST"
jj
    elif azimuth ==180:
        dms_bearing = "DUE NORTH"

    elif azimuth ==270:
        dms_bearing = "DUE EAST"

    else:
        dms_bearing = "NOT APPLICABLE, CHECK INPUT"


# Create line tuple and add to lines list
    line = (counter, distance, dms_bearing)
    lines.append(line)

# Ask for input to continue or stop
    yn = input("DO YOU WANT TO ADD A NEW LINE? [yes/no]  ")
    if yn.lower() =="yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

# Print the lines in a table format using PrettyTable
table = PrettyTable(['LINE NO.', 'DISTANCE', 'BEARING'])
for line in lines:
    table.add_row(line)

print("\n\n")
print(table)
print("----------END----------")





counter = 1
lines = []
sumLat = 0
sumDep = 0    
sumDist = 0
while True:


    print ()
    print ("LINE NO.", counter )

    input_error = False
    while not(input_error):
        distance = input ("Distance:")
        if input_error:
            print("INPUT ERROR")
            continue
        if not (input_error):
            break
