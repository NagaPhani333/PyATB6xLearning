#Clasificaton of triangle
side1 = input("What is your side 1?")
side2 = input("What is your side 2?")
side3 = input("What is your side 3?")

if side1 == side2 == side3:
    print('triangle is equilateral')
elif (side1 ==side2) or (side1 ==side3) or (side2 ==side3):
    print('triangle is isosceles')
elif (side1 != side2) or (side1 !=side3) or (side2 !=side3):
    print('triangle is scalene')
else:
    print('enter correct values')