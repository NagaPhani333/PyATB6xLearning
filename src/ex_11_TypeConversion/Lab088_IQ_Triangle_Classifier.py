# Triangle Classifier:

# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

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



