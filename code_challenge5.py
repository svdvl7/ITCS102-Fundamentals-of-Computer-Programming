num = eval(input("Enter any number:"))
fac = 1

for x in range(num, 0, -1):
    #print(x)
    fac *= x

print("The Factorial of", num, "is", fac)
