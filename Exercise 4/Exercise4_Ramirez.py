"""
Exercise 3 - Functional Programming 
Quinmar Q. Ramirez
2023-14871
BS Geodetic Engineering
"""

from math import cos, sin, radians, sqrt
from prettytable import PrettyTable

class Line:
    def __init__(self, distance, azimuth):
        self.distance = distance  # Initialize distance attribute
        self.azimuth = azimuth    # Initialize azimuth attribute

    def latitude(self): 
        '''
        Compute for the latitude of a given line

        Input:
        distance - float
        azimuth - float

        Output:
        latitude - float
        '''
        latitude = -float(self.distance) * cos(radians(self.azimuth))
        return latitude
    
    def departure(self):
        '''
        Compute for the departure of a given line

        Input:
        distance - float
        azimuth - float

        Output:
        departure - float
        '''
        departure = -float(self.distance) * sin(radians(self.azimuth))
        return departure
    
    def bearing(self):
        '''
        Compute for the DMS bearing of a given angle

        Input:
        azimuth - float

        Output:
        bearing - string
        '''
        if azimuth > 0 and azimuth < 90:
            bearing = 'S {: ^4} W' .format (round(azimuth),3)
        elif azimuth > 90 and azimuth < 180:
            bearing = 'N {: ^4} W' .format (round(180 - azimuth),3)
        elif azimuth > 180 and azimuth < 270:
            bearing = 'N {: ^4} E' .format (round(azimuth - 180),3)
        elif azimuth > 270 and azimuth < 360:
            bearing = 'S {: ^4} E' .format (round(360 - azimuth),3)
        else:
            bearing = "CHECK VALUE"
        return bearing

# Azimuth direction
class Cardinal(Line):
    def __init__(self, distance, azimuth):
        super().__init__(distance, azimuth) 

    # Compute bearing for cardinal directions
    def bearing(self):
        if self.azimuth == 0:
            bearing = "DUE SOUTH"
        elif self.azimuth == 90:
            bearing = "DUE WEST"
        elif self.azimuth == 180:
            bearing = "DUE NORTH"
        elif self.azimuth == 270:
            bearing = "DUE EAST"
        else:
            bearing = "NOT APPLICABLE, CHECK INPUT"
        return bearing
    
# Create a sentinel controlled group
counter = 1
lines = []
sumLat = 0
sumDep = 0    
sumDist = 0

while True:
    print()
    print("LINE NO.", counter)
        
    invalid_syntax = False  
    while not invalid_syntax:  
        distance = input("ENTER DISTANCE: ")
        try:
            distance = float(distance)
            if distance < 0:  # Check if the input is negative
                print("Distance must be a positive number.")
            else:
                invalid_syntax = True  # Valid input, exit the loop
                break  
        except ValueError:
            print("Invalid Syntax. Distance must be a number.")

    azimuth = input ("Azimuth from the South: ") 

    if "-" in str (azimuth): #If user prompts Degree-Minute-Seconds
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees)) + (int(minutes)/60) + (float(seconds)/3600)%360
    else: #If user prompts Decimal.Degrees
        azimuth = float (azimuth)%360
    
    if azimuth % 90 == 0:
        line = Cardinal(distance, azimuth)
    else:
        line = Line(distance, azimuth)

    sumLat += line.latitude()
    sumDep += line.departure()
    sumDist += float(line.distance)    

    lines.append((counter, line.distance, line.bearing(), line.latitude(), line.departure()))

    # Ask for input
    yn = input("ADD NEW LINE?[YES/NO]? ")
    if yn.lower() != "yes" and yn.lower() != "y":
        break
    counter += 1

# Create a PrettyTable instance
table = PrettyTable()
table.field_names = ["LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"]

# Add rows to the table
for line in lines:
    table.add_row([line[0], line[1], line[2], round(line[3], 5), round(line[4], 5)])

# Print the table
print("\n\n")
print(table)

print("SUMMATION OF LAT:", sumLat)
print("SUMMATION OF DEP:", sumDep)
print("SUMMATION OF DIST:", sumDist)

lec = sqrt((sumLat**2) + (sumDep**2))

print("LEC:", lec)
rec = sumDist/lec
print("1: ", round(rec, -3))

print ("-----END-----")

