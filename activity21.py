#WHILE LOOP

dirty = True

while dirty == True:
    confirm = input ("Do you wish to continue washing? (yes/no) ")

    if confirm == 'yes':
        print("Washing Continues...")
        continue

    else:
        print("Washing Stops...")
        break