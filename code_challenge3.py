name = input("Your name ---> ")
fare = int(input("Fare fee ---> "))
student = input("Student or Regular? (Y/N) ")

if student == 'Y' :
	 discount = fare * 0.2
	 new_fare = fare - discount
	 print("Your discount is ", discount)
	 print("Your new fare is ", new_fare)
else:
	 print(name,",your payment is ", fare)