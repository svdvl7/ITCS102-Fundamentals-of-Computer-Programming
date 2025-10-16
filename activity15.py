#STRING FORMATTING

fname = 'Sandra'
mname = 'Reyes'
lname = 'Del Valle'

print(f"My whole name is {fname} {mname} {lname} ")



#FACTORIAL

num = int(input("Enter Number: "))
result = 1

for i in range(num, 0, -1):
    print(f"{result} * {i} = {result * i}")
    result *= i

print(f"Factorial of {num} is {result}")