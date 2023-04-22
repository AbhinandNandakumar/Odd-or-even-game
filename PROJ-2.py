import random
print("LETS BEGIN THE TOSS")
print("*"*40)
choose=input("ODD OR EVEN : ")
print("*"*40)

a=int(input("CHOOSE A NUMBER B/W   1-6  : "))
b=random.randrange(1,7)
print("YOUR NUMBER : {} AND COMPUTER NUMBER : {}".format(a,b))
print("*"*40)

tot_u=0
tot_c=0

if (a+b)%2==0 and choose.lower()=='even':
    m=input("YOU WON THE TOSS, SELECT YOR CHOISE BAT/BOWL : ")
    m1='nil'
    print("*"*40)
elif (a+b)%2==0 and choose.lower()=='odd':
    m1=random.choice(["BAT","BOWL"])
    m='nil'
    print("YOU LOSS THE TOSS, COMPUTER HAS CHOSEN {}".format(m1))
    print("*"*40)
elif (a+b)%2!=0 and choose.lower()=='odd':
    m=input("YOU WON THE TOSS, SELECT YOR CHOISE BAT/BOWL : ")
    print("*"*40)
    m1='nil' 
elif (a+b)%2!=0 and choose.lower()=='even':
    m1=random.choice(["BAT","BOWL"])
    m='nil' 
    print("YOU LOSS THE TOSS, COMPUTER HAS CHOSEN {}".format(m1))
    print("*"*40)

def win():
    if tot_u>tot_c:
        print("USER WON THE GAME")
        print("*"*40)
    elif tot_u<tot_c:
        print("COMPUTER WON THE MATCH")
        print("*"*40)
    else:
        print("MATCH TIED!!!")
        print("*"*40)
    

if m.lower()=='bat':
    while True:
        c=int(input("CHOOSE A NUMBER B/W   1-6  : "))
        d=random.choice([1,2,3,4,5,6])
        print("YOU HAVE CHOOSEN {} AND COMPUTER HAVE CHOOSEN {}".format(c,d))
        print("*"*40)
        if c!=d:
            tot_u+=c
        else:
            print("YOUR BATING OVER AND TARGET FOR COMPUTER IS ",tot_u+1)
            print("*"*40)
            break
    while True:
        c=int(input("CHOOSE A NUMBER B/W   1-6  : "))
        d=random.choice([1,2,3,4,5,6])
        print("YOU HAVE CHOOSEN {} AND COMPUTER HAVE CHOOSEN {}".format(c,d))
        print("*"*40)
        
        if c!=d:
            tot_c+=d
            if tot_c>tot_u:
                break
        else:
            print("COMPUTER BATING OVER AND  SCORE : ",tot_c)
            print("*"*40)
            break
    win()
    
elif m.lower()=='bowl':
    while True:
        c=int(input("CHOOSE A NUMBER B/W   1-6  : "))
        d=random.choice([1,2,3,4,5,6])
        print("YOU HAVE CHOOSEN {} AND COMPUTER HAVE CHOOSEN {}".format(c,d))
        print("*"*40)
        if c!=d:
            tot_c+=d
            
        else:
            print("COMPUTER BATING OVER AND TARGET FOR YOU IS ",tot_c+1)
            print("*"*40)
            break
    while True:
        c=int(input("CHOOSE A NUMBER B/W   1-6  : "))
        d=random.choice([1,2,3,4,5,6])
        print("YOU HAVE CHOOSEN {} AND COMPUTER HAVE CHOOSEN {}".format(c,d))
        print("*"*40)
        if c!=d:
            tot_u+=c
            if tot_u>tot_c:
                break
        else:
            print("YOUR BATING OVER , SCORE : ",tot_u)
            print("*"*40)
            break
    win()

if m1.lower()=='bat':
     while True:
        c=int(input("CHOOSE A NUMBER B/W   1-6  : "))
        d=random.choice([1,2,3,4,5,6])
        print("YOU HAVE CHOOSEN {} AND COMPUTER HAVE CHOOSEN {}".format(c,d))
        print("*"*40)
        if c!=d:
            tot_c+=d
        else:
            print("COMPUTER BATING OVER AND TARGET FOR YOU IS ",tot_c+1)
            print("*"*40)
            break
     while True:
        c=int(input("CHOOSE A NUMBER B/W   1-6  : "))
        d=random.choice([1,2,3,4,5,6])
        print("YOU HAVE CHOOSEN {} AND COMPUTER HAVE CHOOSEN {}".format(c,d))
        print("*"*40)
        if c!=d:
            tot_u+=c
            if tot_u>tot_c:
                break
        else:
            print("YOUR BATING OVER , SCORE : ",tot_u)
            print("*"*40)
            break
     win()

elif m1.lower()=='bowl':
    while True:
        c=int(input("CHOOSE A NUMBER B/W   1-6  : "))
        d=random.choice([1,2,3,4,5,6])
        print("YOU HAVE CHOOSEN {} AND COMPUTER HAVE CHOOSEN {}".format(c,d))
        print("*"*40)
        if c!=d:
            tot_u+=c
        else:
            print("YOUR BATING OVER AND TARGET FOR COMPUTER IS ",tot_u+1)
            print("*"*40)
            break
    while True:
        c=int(input("CHOOSE A NUMBER B/W   1-6  : "))
        d=random.choice([1,2,3,4,5,6])
        print("YOU HAVE CHOOSEN {} AND COMPUTER HAVE CHOOSEN {}".format(c,d))
        print("*"*40)
        if c!=d:
            tot_c+=d
            if tot_c>tot_u:
                break
        else:
            print("COMPUTER BATING OVER AND  SCORE : ",tot_c)
            print("*"*40)
            break
    win()






    
    
