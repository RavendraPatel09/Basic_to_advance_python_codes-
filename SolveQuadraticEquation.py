import math
a, b, c = 1, 5, 6
d = b**2 - 4*a*c
root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b - math.sqrt(d)) / (2*a)
print("Roots:", root1, "and", root2)