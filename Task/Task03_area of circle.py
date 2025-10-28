
#area of circle using different methods

import math

radius = float(input("Please enter radius : ")) #116
print("Radius of circle is : ", radius)
area = 3.14*(radius**2) #using operators
area1 = 3.14*pow(radius, 2) #using pow function
area2 = math.pi* pow(radius, 2) #using math functions
print("Area of circle is : ", str(area))
print(f"Area of circle is  -> using str data formating : {area:.3f}" )
print(f"Area of circle is  -> using str data formating : {area1:.1f}")
print(f"Area of circle is  -> using str data formating : {area2:.2f}")
