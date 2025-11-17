# LIST OPERATIONS

print("Names")
names = ['Gabo', 'Vani', 'Chippy', 'Dark Shadow']
#no.        0       1        2            3 
print(names)

print("\nThird Item")
# Print the third item
print(names[2])

print("\nFirst 3 Items")
# Print the first three items
print(names[0 : 3])

print("\nAppend")
# Add a new name to the end of the list
names.append('Hammy')
print(names)

print("\nPop")
# Remove the last name
names.pop()
print(names)

print("\nInsert")
# Insert a name at index 2
names.insert(1, 'Mochi')
print(names)

print("\nRemove")
# Remove a name by value
names.remove('Vani')
print(names)

print("\nLen")
# Print the total number of names
print(f'you have {len(names)} names')

print("\nSort")
# Sort the list alphabetically
names.sort()
print(names)

print("\nReverse")
# Reverse the list
names.reverse()
print(names)
