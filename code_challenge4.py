name = input("Hi, what's your name? ")
print("Welcome", name, "to a food recommendation program!")
print("Answer a few questions to find what you're really craving for.")

taste = input("What taste would you like? (Sweet, Salty, Sour) ")

if taste == 'Sweet':
    texture = input("To drink or chew? ")

    if texture == 'drink':
        temp = input("Cold or hot? ")

        if temp == 'cold':
            flavor = input("Choose what type (Coffee, Soft drink, Bobba, Fruit): ")
            if flavor == 'Coffee':
                print("I recommend you the Mocha Frappuccino.")
            elif flavor == 'Soft drink':
                print("I recommend you some Cola.")
            elif flavor == 'Bobba':
                print("I recommend you Wintermelon Milk Tea.")
            elif flavor == 'Fruit':
                print("I recommend you Mango Juice.")
            else:
                print("I recommend you some Iced Lemonade.")
        
        elif temp == 'hot':
            flavor = input("Choose what type (Coffee, Tea, Chocolate): ")
            if flavor == 'Coffee':
                print("I recommend you Hot Cappuccino.")
            elif flavor == 'Tea':
                print("I recommend you Chamomile Tea.")
            elif flavor == 'Chocolate':
                print("I recommend you Hot Chocolate.")
            else:
                print("I recommend you a warm Honey Drink.")
        else:
            print("I recommend you Hot Milk.")

    elif texture == 'chew':
        typee = input("Fruit, ice cream, bread? ")

        if typee == 'fruit':
            print("I recommend you some Strawberries.")
        elif typee == 'ice cream':
            print("I recommend you Cookies and Cream Ice Cream.")
        elif typee == 'bread':
            print("I recommend you some Cinnamon Rolls.")
        else:
            print("I recommend you a Chocolate Bar.")
    else:
        print("I recommend you a sweet lollipop.")

elif taste == 'Salty':
    texture2 = input("Crunchy or soft? ")

    if texture2 == 'crunchy':
        type2 = input("Choose what type (Snacks, Vegetables, Meat): ")

        if type2 == 'Snacks':
            print("I recommend you Potato Chips.")
        elif type2 == 'Vegetables':
            print("I recommend you Roasted Seaweed.")
        elif type2 == 'Meat':
            print("I recommend you Crispy Bacon.")
        else:
            print("I recommend you Salted Crackers.")

    elif texture2 == 'soft':
        type2 = input("Choose what type (Soup, Meat, Vegetables): ")

        if type2 == 'Soup':
            print("I recommend you Chicken Noodle Soup.")
        elif type2 == 'Meat':
            print("I recommend you Pork Adobo.")
        elif type2 == 'Vegetables':
            print("I recommend you Mashed Potatoes.")
        else:
            print("I recommend you a savory Omelette.")
    else:
        print("I recommend you Salted Nuts.")

elif taste == 'Sour':
    type3 = input("Choose what type (Fruit, Drink, Candy): ")

    if type3 == 'Fruit':
        print("I recommend you Green Mango with Salt.")
    elif type3 == 'Drink':
        print("I recommend you Calamansi Juice.")
    elif type3 == 'Candy':
        print("I recommend you Sour Gummies.")
    else:
        print("I recommend you Lemon Slices.")

else:
    print("Sorry, I don’t have a recommendation for that taste. Try Sweet, Salty, or Sour!")
