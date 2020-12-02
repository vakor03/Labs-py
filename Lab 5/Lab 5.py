print("Input your n: ", end="")
n = int(input())
maxSumOfDivs = 1
numWithMaxDivs = 1
for i in range (1, n+1):
    sumOfDivs = 0

    for j in range(1, i+1):
        if i % j == 0:
            sumOfDivs += j

    print(i, "with sum of divs", sumOfDivs)

    if sumOfDivs > maxSumOfDivs:
        maxSumOfDivs = sumOfDivs
        numWithMaxDivs = i

print()
print(numWithMaxDivs, "has max sum of divs:", maxSumOfDivs)

