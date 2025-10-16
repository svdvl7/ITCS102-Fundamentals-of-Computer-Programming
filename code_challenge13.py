#ODD NUMBER SUMMATION

name = input("input your name----> ")
print("-------------------------------")
print("ODD NUMBER SUMMATION, press 0 to stop")
print("-------------------------------")

con = True
odd = ""
sum = 0
odd_count = 0

while con == True:
    num = eval(input("Input a random number----> "))
    
    if num %2 == 1:
        sum += num
        odd += str(num) + " "
        odd_count += 1
        continue

    elif num == 0:
        print("PROGRAMM STOPS!!!")
        break
    
    else:
        if num %2 == 0:
            print("EVEN NUMBER DETECTED, continue")
        else:
            print("INVALID INPUT")
        continue

print(f"Hi {name}, sum of all ODD number is {sum}")
print(f"You entered {odd_count} odd number/s")
print(f"ODD Numbers detected included the ff {odd}")
