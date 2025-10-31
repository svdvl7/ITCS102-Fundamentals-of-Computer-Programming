#ANIME TITLES

# Objective:
# - Create and modify a list
# - Use a while loop for repeated input
# - Use a stopping condition

print("🎯 Collecting Favorite Anime Titles 🎯")
print("Type 'stop' when you're done.\n")

anime_list = []

while True:
    anime = input("Enter your favorite anime title: ")

    if anime.lower() == "stop":
        break

    anime_list.append(anime)

print("\nYour favorite anime titles are:")
for title in anime_list:
    print(f"- {title}")

print("\nThank you for sharing your favorites!")
