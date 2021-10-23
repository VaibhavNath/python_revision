#door game , questions and more

'''import random

def doorgame():
    life= 5
    while life> 0:
        door=random.randint(1,5)
        print("door:",door)  #for debugging
        print("Life:",life)
        life -= 1
        guess=int(input("enter a guess of door:"))
        if guess != door:
            if life>0:
                print("guess again")
                continue
            else:
                print("you loose all of your life.the correct door was" + str(door))
            
        else:
            print("well done,you managed to escape")
        print("do you want to play again?")
        q=input("yes or No: ").lower()[0]
        if q=='y':
            life = 5
        else:
            life = 0
    else:
        print("game over")
        print("thank you for playing")


doorgame()  '''