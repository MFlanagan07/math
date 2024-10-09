#this is my math library


import math
pi_value = math.pi
def Area_Circle_radius(radius,pi_value):
    Area_Circle = pi_value*radius**2
    return(Area_Circle)

def Area_Circle_diameter(diameter):
    int(diameter)
    radius = diameter / 2
    
    Area_Circle = pi_value*radius**2
    return(Area_Circle)

def Perimeter_Diameter(diameter):
    int(diameter)
    radius = diameter / 2
    Perimeter_Circle = 2*pi_value*radius
    return(Perimeter_Circle)

def Perimeter_Radius(radius):
    Perimeter_Circle = 2*pi_value*radius
    return(Perimeter_Circle)

def Area_Rectangle(length,width):
    area = length * width
    return(area)

def Perimeter_Rectangle(length,width):
    perimeter = 2*length + 2*width
    return(perimeter)
