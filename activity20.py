#  DIAMOND

for i in range (1,11,1):
    for x in range(10,i,-1):
        print(' ', end = '')
    for y in range(1,i,1):
        print('n', end = '')
    for b in range (1,i,1):
        print('n', end = '')
    print()

for new in range (1,11,1):
    for n in range(new,1,-1):
        print(' ', end = '')
    for m in range(10,new,-1):
        print('n', end = '')
    for g in range (10,new,-1):
        print('n', end = '')
    print()