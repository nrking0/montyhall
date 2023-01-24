import random

ywins = 0
ylose = 0
nwins = 0
nlose = 0
n = 10000
print(n, 'trials')


for switch in range(2):
    for j in range(n):
        doors = [1,2,3]
        win = random.choice(doors)


        #choice = input("Choose a door 1-3\n")
        choice = random.choice(doors)

        #print(doors, win, choice)

        copy = [x for x in doors if x != int(choice) and x != win]

        wrong = random.choice(copy)
        #print(wrong, "is not the right choice")

         #switch = input("Switch? y/n\n")

        if switch:
            choice = next(x for x in doors if x != wrong and x != choice)

            
        if choice == win:
            #print('You Win!')
            if switch:
                ywins = ywins + 1
            else:
                nwins = nwins + 1
        else:
            #print('You Lose!', win, 'was correct!')
            if switch:
                ylose = ylose + 1
            else:
                nlose = nlose + 1
                

wswitch = round((ywins / (ylose + ywins)) * 100, 2)
wstay = round((nwins / (nlose + nwins)) * 100, 2)
print('When switching doors we won ', wswitch, ' percent of the time.')
print('When staying we won ', wstay, ' percent of the time.')
