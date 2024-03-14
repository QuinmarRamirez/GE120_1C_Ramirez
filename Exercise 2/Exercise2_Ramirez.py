"""
Exercise 2 - Control Structures
Quinmar Q. Ramirez
2023-14871
BS Geodetic Engineering
"""

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
    azimuth = float(input("ENTER AZIMUTH FROM THE SOUTH (in decimal degrees): ")) 

# Converting Decimal Degrees to Degrees-Minutes-Seconds
    degrees = int(azimuth)
    remainder = abs(azimuth - degrees) * 60
    minutes = int(remainder)
    seconds = (remainder - minutes) * 60

    dms_azimuth = "{}-{}-{:.2f}" .format(degrees, minutes, seconds)

# Assigning Azimuth to Bearing
    if azimuth > 0 and azimuth < 90:
        bearing = 'S {: ^10} W' .format(dms_azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {: ^10} W' .format(180 - degrees)
    elif azimuth > 180 and azimuth < 270:
        bearing = 'N {: ^10} E' .format(degrees -180)
    elif azimuth > 270 and azimuth < 360:
        bearing = 'S {: ^10} E' .format(360 - degrees)
    elif azimuth ==0:
        bearing = "DUE SOUTH"
    elif azimuth ==90:
        bearing = "DUE WEST"
    elif azimuth ==180:
        bearing = "DUE NORTH"
    elif azimuth ==270:
        bearing = "DUE EAST"
    else:
        bearing = "NOT APPLICABLE, CHECK INPUT"

# Create line tuple and add to lines list
    line = (counter, distance, bearing)
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

        
 





  