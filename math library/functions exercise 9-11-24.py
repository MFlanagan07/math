import math
import myCircleArea

pi_value = math.pi
print("1. Area Of Circle\n2. Perimeter of circle\n3. Area of Rectangle\n4. Perimeter of Circle")






def Area_Rectangle(length,width):
    area = length * width
    return(area)

def Perimeter_Rectangle(length,width):
    perimeter = 2*length + 2*width
    return(perimeter)















menu_choice = input("")




if menu_choice == "1":
    print("Do you have the\n1. Diameter\n2. Radius")
    diarad = input("")
    if diarad == "1":
        print("Enter the diameter of the circle")
        dia = int(input(""))
        Area = Area_Circle_diamater(dia)
    elif diarad == "2":
        
        print("Enter the radius of the circle")
        rad = int(input(""))
        Area = myCircleArea.Area_Circle_radius(rad,pi_value)
    print("the area of that circle is",round(Area,2),"units sq.")
        
elif menu_choice == "2":
    print("Do you have the\n1. Diameter\n2. Radius")
    diarad = input("")
    if diarad == "1":
        print("Enter the diameter of the circle")
        dia = int(input(""))
        perimeter = Perimeter_Diameter(dia)
        
    elif diarad == "2":
        print("Enter the radius of the circle")
        rad = int(input(""))
        perimeter = myCircleArea.Perimeter_Radius(rad)
    print("the perimeter of that circle is",round(perimeter,2),"units")
        
elif menu_choice == "3":
    leng = int(input("Enter the length of the Rectangle: "))
    width = int(input("Enter the width of the Rectangle: "))
    Area = Area_Rectangle(leng,width)
    print("The Area of that rectangle is",round(Area,2),"units sq.")
    
elif menu_choice == "4":
    print("test")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    