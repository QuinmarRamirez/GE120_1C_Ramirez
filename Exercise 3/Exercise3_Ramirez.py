"""
Exercise 3 - Functional Programming
Quinmar Q. Ramirez
2023-14871
BS Geodetic Engineering
"""


from math import cos, sin, radians 

def getLatitude(distance, azimuth):
    '''
    Compute for the latitude of a given line.

    Inout:
    distance - float
    azimuth - float

    Output:
    latitude - float
    '''

    latitude = -distance * cos(radians(azimuth))

    return latitude

lat = getLatitude(12,45)


print(lat)


def getDeparture(distance, azimuth):
    '''
    Compute for the latitude of a given line.

    Inout:
    distance - float
    azimuth - float

    Output:
    departure - float
    '''

    departure = -distance * sin(radians(azimuth))

    return departure

lat = getLatitude(12,45)
dep = getDeparture(12,160)
print(lat,dep)

def azimuthToBearing(distance, azimuth):
    '''
    Compute for the DMS bearing of a given angle.

    Inout:
    distance - float
    azimuth - float

    Output:
    departure - float
    '''

    departure = -distance * sin(radians(azimuth))





