x = float(input())
y = float(input())
if x >= -1:
    isInShape = 1
elif (((x+2)**2 + y**2 >= 1) and ((x+2)**2 + y**2 <= 4)):
    isInShape = 1
else:
    isInShape = 0

if isInShape == 1:
    Output = "Точка належить площині"
else:
    Output = "Точка не належить площині"
print(Output)
