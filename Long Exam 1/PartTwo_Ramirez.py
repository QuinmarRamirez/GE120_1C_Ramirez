"""
Direct Levelling Computations
Quinmar Q. Ramirez
2023-14871
BS Geodetic Engineering

This program performs direct levelling computations. This also determines the Geodetic Control Order of the levelling survey
given its vertical accuracy. 
"""

# Initializing Variables
levelling_table = ()
tp_counter = 1
levelling_table = []
total_distance = 0.0

# Defining a function named ' floatInput'
def floatInput(prompt):
    '''
    This function asks the user to input a prompt. 

    Input:
    prompt - float
    Output:
    User input - float
    '''
    while True:
        try:
            user_input = float(input(prompt))

            return user_input

        except ValueError:
            print("Please enter a valid number.")

# Asking for the initial elevation BM1 using floatInput function
BM1 = floatInput("ENTER THE INITIAL ELEVATION (BM1): ")

# Create a variable to store the running elevation of the survey
running_elevation = BM1  

# Asking the User
while True:
    print()
    print("STATION: TP", tp_counter)
    Backsight = floatInput("ENTER BACKSIGHT MEASUREMENT: ")
    Foresight = floatInput("ENTER FORESIGHT MEASUREMENT: ")
    distance = floatInput("ENTER DISTANCE: ")
    
    Height_of_the_Instrument = running_elevation + Backsight
    ELEVATION = Height_of_the_Instrument  - Foresight
    total_distance += distance
    
# Create tuple
    levelling_table.append((tp_counter, Backsight, Foresight, distance, ELEVATION))

# Ask for input to continue or stop
    yn = input("DO YOU WANT TO TO CREATE A NEW TURNING POINT? [yes/no]  ")
    if yn.lower() =="yes" or yn.lower() == "y":
        tp_counter = tp_counter + 1
        continue
    else:
        break

# Printing
print("\nLevelling Table:")
print("--------------------------------------------------------")
print("Backsight | Height of Instrument | Foresight | Elevation")
print("--------------------------------------------------------")

for data in levelling_table:
    print("{:<10} {:<21} {:<10} {:<10}".format(*data))
print("--------------------------------------------------------")
print("Total Distance:", total_distance)
print("----------END----------")
