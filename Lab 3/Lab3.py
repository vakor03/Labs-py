x, eps = input("Input your x: "), input("Input your eps: ")
n = 1
lastEl = x
Sh = x
while eps < lastEl:
    lastEl *= x**2/(2*n * (2*n + 1))
    Sh += lastEl
    n += 1
print()