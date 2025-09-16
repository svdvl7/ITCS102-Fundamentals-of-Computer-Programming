odd_sum = 0
odd_found = False  # to track if any odd number is entered

for i in range(7):
    num = int(input("Enter a number: "))
    if num % 2 != 0:  # check if odd
        odd_sum += num
        odd_found = True

if odd_found:
    print("The sum of all odd numbers is", odd_sum)
else:
    print("At least put an odd number!")
