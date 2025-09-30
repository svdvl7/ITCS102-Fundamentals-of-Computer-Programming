temp = eval(input("Enter temperature here -----> "))

if temp <= 0:
    print("The temperature is Below Freezing Point")
if temp >= 1 and temp <= 15:
    print("The temperature is Extremely Cold")
if temp >= 16 and temp <= 30:
    print("The Temperature is Cold")
if temp >= 31 and temp <= 38:
    print("The Temperature is Lukewarm")
if temp >= 39 and temp <= 42:
    print("The Tempperature is Warm")
if temp >= 43 and temp <= 50:
	print("The temperature is Hot")
if temp >= 51 and temp <= 60:
	print("The temperature is Extremely Hot")
if temp >= 61:
	print("The temperature is Burning")