# MULTIPLICATION TABLE MAKER

num = int(input("Enter a number: "))

print("\nMultiplication table for", num, ":")

for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)
