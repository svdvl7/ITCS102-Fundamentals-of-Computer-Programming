#RANDOM INTIGER

import random

random_number = random.randint(1, 50)
g = True

print("🎰 Welcome to the Mini Lottery! 🎉")
print("🔢 Guess the lucky number from 1 to 50")
print("🎯 You got 3 tries")
print("Good Luck 😁🍀")

tries = 3

while g:
    number = int(input("👉 Input number here --> "))
    if number != random_number:
        tries -= 1
        if tries > 0:
            print(f"❌ Wrong number! You have {tries} trie/s left. 🔄")
            continue
        else:
            print("💀 No tries left. Game Over.")
            print(f"🎯 The lucky number was {random_number}")
            break
    elif number == random_number:
        print("🎉✨ JACKPOT! You guessed the lucky number! ✨🎉")
        print("💰 You won 1 million pesos! Go ahead and claim your prize! 🤑🎁")
        break

print(f"🔚 Tries remaining: {tries}")