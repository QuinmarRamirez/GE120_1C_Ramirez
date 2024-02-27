"""
Hi, this is exercise 1. 
I am Quinmar Ramirez
2023-14871
BS Geodetic Engineering
"""

dms = 118.42069

#Getting degree
degree = int(dms)
print("DEGREE:", degree)

#Getting minutes
minutes = (dms - degree) * 60
minutes_fractional = int(minutes)
print("MINUTES", minutes)

#Getting seconds
seconds = (minutes - minutes_fractional) * 60
print("SECONDS", seconds)

#The Degree-Minute-Second 
print("DMS: "+ str(degree) + "-" +str(minutes_fractional) + "-" + str(round(seconds, 2)))

#Converting DMS to DD
dms = "118-25-14.48"
values = dms.split("-")

degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

dd= degrees + (minutes/60) +(seconds/3600)

#The Decimal Degree
print("DD:", round(dd,6))


