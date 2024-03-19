"""
Exercise 3 - Functional Programming
Quinmar Q. Ramirez
2023-14871
BS Geodetic Engineering
"""


# from math import cos, sin, radians, sqrt

# def getLatitude (distance, azimuth):
#     '''
#     Computing for the Latitude of a given line
#     Input:
#     distance - float
#     azimuth - float
#     Output:
#     Latitude - float
#     '''
#     latitude = -distance * cos (radians(azimuth))

#     return latitude

# def getDeparture (distance, azimuth):
#     '''
#     Computing for the Departure of a given line
#     Input:
#     distance - float
#     azimuth - float
#     Output:
#     Departure - float
#     '''
#     departure = -distance * sin (radians(azimuth))

#     return departure


# def azimuthToBearing (azimuth):
#     '''
#     Computing for the DMS bearing of a given angle
#     Input:
#     azimuth - float
#     Output:
#     bearing - string
#     '''


# counter = 1
# lines = []
# sumLat = 0
# sumDep = 0    
# sumDist = 0
# while True:


#     print ()
#     print ("LINE NO.", counter )

#     input_error = False
#     while not(input_error):
#         distance = input ("Distance:")
#         if input_error:
#             print("INPUT ERROR")
#             continue
#         if not (input_error):
#             break
    
#     azimuth = input ("Azimuth from the South (DD or DMS): ") 
#     bearing = azimuthToBearing(azimuth)
#     if "-" in str(azimuth): 
#         degrees, minutes, seconds = azimuth.split("-")
#         azimuth = (int(degrees)) + (int(minutes)/60) + (float(seconds)/3600)%360
#     else:
#         azimuth = float (azimuth)%360

#     if azimuth > 0 and azimuth < 90:
#         bearing = 'S {: ^10} W' .format (azimuth)
#     elif azimuth > 90 and azimuth < 180:
#         bearing = 'N {: ^10} W' .format (180 - azimuth)
#     elif azimuth > 180 and azimuth < 270:
#         bearing = 'N {: ^10} E' .format (azimuth - 180)
#     elif azimuth > 270 and azimuth < 360:
#         bearing = 'S {: ^10} E' .format (360 - azimuth)
#     elif azimuth == 0:
#         bearing = "DUE SOUTH"
#     elif azimuth == 90:
#         bearing = "DUE WEST"
#     elif azimuth == 180:
#         bearing = "DUE NORTH"
#     elif azimuth == 270:
#         bearing = "DUE EAST"
#     else:
#         bearing = "UNKNOWN"



#     lat = getLatitude(azimuth=float(azimuth), distance=float(distance))
#     dep = getDeparture(azimuth=float(azimuth), distance=float(distance))

#     sumLat += lat
#     sumDep += dep
#     sumDist += float(distance)

#     line = (counter, distance, bearing, lat, dep,)
#     lines.append(line)

#     yn = input("Add new line? ")
#     if yn.lower() == "yes" or yn.lower() == "y":
#         counter = counter + 1
#         continue
#     else:
#         break
# print(line)
# print ("\n\n")
# print ('{: ^10} {: ^10} {: ^15} {: ^15} {: ^18}' .format ("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))
# for line in lines:
#     print ('{: ^10} {: ^10} {: ^15} {: ^15} {: ^18}' .format (line [0], line [1], line [2], line [3], line [4]))

# print("SUMMATION OF LAT:", sumLat)
# print("SUMMATION OF DEP:", sumDep)
# print("SUMMATION OF DIST:", sumDist)

# lec = sqrt((sumLat**2) + (sumDep**2))

# print ("LEC:", lec)
# rec = sumDist/lec
# print("1: ", round(rec, -3))

# constCorrLat = -sumLat/sumDist
# constCorrDep = -sumDep/sumDist


# corr_lat = constCorrLat * float(line[1])
# corr_dep = constCorrDep * float(line[1])

# adjLat = line[3] + corr_lat
# adjDep = line[4] + corr_dep

# print ("Adjusted Latitude: ", adjLat)
# print ("Adjusted Departure: ", adjDep)

# print ("-----END-----")


# Define a function named 'calculate_rectangle_area' that takes 'length' and 'width' as parameters
# def calculate_rectangle_area(length, width):
#     # Calculate the area of the rectangle using the formula: area = length * width
#     area = length * width
#     # Return the calculated area
#     return area

# # Prompt the user to enter the dimensions of the rectangle
# # length = float(("Enter the length of the rectangle: "))
# # width = float(("Enter the width of the rectangle: "))

# # Call the 'calculate_rectangle_area' function with user-provided length and width
# # The returned area is assigned to the variable 'rectangle_area'
# rectangle_area = calculate_rectangle_area(length, width)

# # Display the calculated area of the r
# print(f"The area of the rectangle with length {length} and width {width} is: {rectangle_area}")


def hey(word1, ilang_beses):

    print(word1.upper() + word1[-1]*5 + "!!!!")

hey("jem", 2)