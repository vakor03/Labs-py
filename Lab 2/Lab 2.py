x, y = float(input("Input x: ")), float(input("Input y: "))

if x >= -1:
    isInShape = 1
elif 1 <= (x+2)**2 + y**2 <= 4:
    isInShape = 1
else:
    isInShape = 0

if isInShape == 1:
    Output = "Точка належить площинi"
else:
    Output = "Точка не належить площинi"

print(Output)
