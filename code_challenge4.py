name = input("Hi, what's your name? ")
print("Welcome", name, "to an Anime/Manga Recommender!")
print("Answer a few questions to find what you might enjoy.")

genre = input("What genre do you like? (Action, Comedy, Horror, Romance, Drama): ")

if genre == 'Action':
    length = input("Do you want Short, Medium, or Long series? ")

    if length == 'Short':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Black Lagoon' (2006).")
        elif decade == '2010s':
            print("I recommend 'One Punch Man' (2015).")
        elif decade == '2020s':
            print("I recommend 'Jujutsu Kaisen' (2020).")
        else:
            print("I recommend 'Soul Eater' (2008).")

    elif length == 'Medium':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Naruto Shippuden' (2007).")
        elif decade == '2010s':
            print("I recommend 'My Hero Academia' (2016).")
        elif decade == '2020s':
            print("I recommend 'Demon Slayer' (2019).")
        else:
            print("I recommend 'Blue Exorcist' (2011).")

    elif length == 'Long':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Bleach' (2004).")
        elif decade == '2010s':
            print("I recommend 'Attack on Titan' (2013).")
        elif decade == '2020s':
            print("I recommend 'Boruto' (2020).")
        else:
            print("I recommend 'Black Clover' (2017).")
    else:
        print("I recommend 'Dragon Ball Z' (classic).")

elif genre == 'Comedy':
    length = input("Do you want Short, Medium, or Long series? ")

    if length == 'Short':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'School Rumble' (2004).")
        elif decade == '2010s':
            print("I recommend 'Daily Lives of High School Boys' (2012).")
        elif decade == '2020s':
            print("I recommend 'KonoSuba: Legend of Crimson' (2020).")
        else:
            print("I recommend 'Ouran High School Host Club' (2006).")

    elif length == 'Medium':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Gintama' (2006).")
        elif decade == '2010s':
            print("I recommend 'Nichijou' (2011).")
        elif decade == '2020s':
            print("I recommend 'Komi Can’t Communicate' (2021).")
        else:
            print("I recommend 'Servant x Service' (2013).")

    elif length == 'Long':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Hayate the Combat Butler' (2007).")
        elif decade == '2010s':
            print("I recommend 'Gintama (2011–2017)'.")
        elif decade == '2020s':
            print("I recommend 'Spy x Family' (2022).")
        else:
            print("I recommend 'Working!!' (2010).")
    else:
        print("I recommend 'Excel Saga' (classic).")

elif genre == 'Horror':
    length = input("Do you want Short, Medium, or Long series? ")

    if length == 'Short':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Hellsing' (2001).")
        elif decade == '2010s':
            print("I recommend 'Another' (2012).")
        elif decade == '2020s':
            print("I recommend 'Mieruko-chan' (2021).")
        else:
            print("I recommend 'Shiki' (2010).")

    elif length == 'Medium':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Elfen Lied' (2004).")
        elif decade == '2010s':
            print("I recommend 'Tokyo Ghoul' (2014).")
        elif decade == '2020s':
            print("I recommend 'High-Rise Invasion' (2021).")
        else:
            print("I recommend 'Paranoia Agent' (2004).")

    elif length == 'Long':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Blood+' (2005).")
        elif decade == '2010s':
            print("I recommend 'Ajin: Demi-Human' (2016).")
        elif decade == '2020s':
            print("I recommend 'Chainsaw Man' (2022).")
        else:
            print("I recommend 'Higurashi no Naku Koro ni' (2006).")
    else:
        print("I recommend 'Vampire Hunter D' (classic).")

elif genre == 'Romance':
    length = input("Do you want Short, Medium, or Long series? ")

    if length == 'Short':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Lovely★Complex' (2007).")
        elif decade == '2010s':
            print("I recommend 'Your Lie in April' (2014).")
        elif decade == '2020s':
            print("I recommend 'Horimiya' (2021).")
        else:
            print("I recommend 'Golden Time' (2013).")

    elif length == 'Medium':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Clannad' (2007).")
        elif decade == '2010s':
            print("I recommend 'Toradora!' (2008).")
        elif decade == '2020s':
            print("I recommend 'My Dress-Up Darling' (2022).")
        else:
            print("I recommend 'Anohana' (2011).")

    elif length == 'Long':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Honey and Clover' (2005).")
        elif decade == '2010s':
            print("I recommend 'Kimi ni Todoke' (2009).")
        elif decade == '2020s':
            print("I recommend 'Rent-A-Girlfriend' (2020).")
        else:
            print("I recommend 'Nodame Cantabile' (2007).")
    else:
        print("I recommend 'Boys Be...' (classic romance).")

elif genre == 'Drama':
    length = input("Do you want Short, Medium, or Long series? ")

    if length == 'Short':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Ergo Proxy' (2006).")
        elif decade == '2010s':
            print("I recommend 'Anohana' (2011).")
        elif decade == '2020s':
            print("I recommend 'March Comes in Like a Lion' (2020s ongoing).")
        else:
            print("I recommend 'Paranoia Agent' (2004).")

    elif length == 'Medium':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Monster' (2004).")
        elif decade == '2010s':
            print("I recommend 'Psycho-Pass' (2012).")
        elif decade == '2020s':
            print("I recommend 'Vinland Saga Season 2' (2023).")
        else:
            print("I recommend 'Terror in Resonance' (2014).")

    elif length == 'Long':
        decade = input("Which decade? (2000s, 2010s, 2020s): ")
        if decade == '2000s':
            print("I recommend 'Nana' (2006).")
        elif decade == '2010s':
            print("I recommend 'Shouwa Genroku Rakugo Shinjuu' (2016).")
        elif decade == '2020s':
            print("I recommend 'Ousama Ranking' (2021).")
        else:
            print("I recommend 'Rainbow' (2010).")
    else:
        print("I recommend 'Grave of the Fireflies' (classic drama).")

else:
    print("Sorry, I don’t have a recommendation for that genre. Try Action, Comedy, Horror, Romance, or Drama!")
