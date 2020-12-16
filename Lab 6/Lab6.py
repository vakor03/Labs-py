def Ln(x,eps):        
	if (x == 0):
		return  "You can't find ln0"
	currEl = x - 1
	n = 2
	sum = currEl
	while (abs(currEl) > eps):
		currEl = (-1)**(n-1) * (x - 1)**n / float(n)
		sum += currEl
		n+=1            
	return sum

def FindY(x, eps):            
	res = 0
	if (x < 2):
		res = Ln(x, eps) + Ln(x/2, eps)
	elif (x >= 2):
		res = Ln(x/2 - 1, eps)
	return res

print("Input your eps: ")
eps = float(input())
for i in range(1, 7, 1):            
	print("x =", i/2, "Ln =", FindY(i/2, eps))