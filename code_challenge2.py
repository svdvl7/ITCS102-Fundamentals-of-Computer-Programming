amount = int(input("Enter amount to deposit ---> ₱"))

print("Here is a breakdown of the deposit amount:")

thousands = amount // 1000
amount = amount % 1000

fivehundreds = amount // 500
amount = amount % 500

twohundreds = amount // 200
amount = amount % 200

onehundreds = amount // 100
amount = amount % 100

fifty = amount // 50
amount = amount % 50

twenty = amount // 20
amount = amount % 20

ten = amount // 10
amount = amount % 10

five = amount // 5
amount = amount % 5

one = amount // 1
amount = amount % 1

print("₱1,000 -", thousands)
print("₱500 -", fivehundreds)
print("₱200 -", twohundreds)
print("₱100 -", onehundreds)
print("₱50 -", fifty)
print("₱20 -", twenty)
print("₱10 -", ten)
print("₱5 -", five)
print("₱1 -", one)