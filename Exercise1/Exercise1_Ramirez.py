"""
Exercise 1 - Procedural Programming
Quinmar Q. Ramirez
2023-14871
BS Geodetic Engineering
"""

dd = 118.42069

# Getting degrees
degree = int(dd)
# print("DEGREES:", degree)

# Getting minutes
minutes = (dd - degree) * 60
minutes_fractional = int(minutes)
# print("MINUTES", minutes)

# Getting seconds
seconds = (minutes - minutes_fractional) * 60
# print("SECONDS", seconds)

# The Degree-Minute-Second 
print("DMS: "+ str(degree) + "-" +str(minutes_fractional) + "-" + str(round(seconds, 2)))

# Converting DMS to DD
dms = "118-25-14.48"
values = dms.split("-")

degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

dd= degrees + (minutes/60) +(seconds/3600)

# The Decimal Degree
print("DD:", round(dd,6))