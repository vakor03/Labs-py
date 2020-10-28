import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
angle = float(input("Enter angle between a and b: "))

angleInRad = math.pi * angle / 180
sinAngle = math.sin(angleInRad)
S = a * b * 0.5 * sinAngle

print("S = ", S)
