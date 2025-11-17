# DICTIONARY

# List of ice cream flavors
ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough']

# Dictionary of ice cream flavors with descriptions
flavor_dictionary = {
    'Vanilla': 'classic and sweet',
    'Chocolate': 'rich and creamy',
    'Strawberry': 'fruity and refreshing',
    'Mint': 'cool and fresh',
    'Cookie Dough': 'fun with chunks'}

print("Available ice cream flavors:")
for flavor in ice_cream_flavors:
    print(f"- {flavor}")

ur_flavor = input("Choose a flavor from the list above: ")

if ur_flavor in flavor_dictionary:
    print(f"{ur_flavor}: {flavor_dictionary[ur_flavor]}")
else:
    print(f"{ur_flavor} is not in the list.")
    # Optionally add the new flavor
    add = input("Do you want to add it? (yes/no): ").lower()
    if add == 'yes':
        description = input(f"Enter a description for {ur_flavor}: ")
        flavor_dictionary[ur_flavor] = description
        ice_cream_flavors.append(ur_flavor)
        print(f"{ur_flavor} added! Current flavors: {ice_cream_flavors}")


