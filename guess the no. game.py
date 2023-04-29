import random
print("rule of game-you have minimum attempt to win the game is 15")

guess=random.randint(1,100)
s=15

attempt=15
for i in range (1,16):
    n=int(input("enter the number that u want to guess "))
    
    if(n==guess):
        print("you win the game")
        
        break
    elif(n>guess):
        print("the no. u gues is large")
        s=s-1
        attempt=attempt-1
        print("your remaining attempt",attempt)
    elif(n<guess):
        print("the no. u guess is small")
        s=s-1
        attempt=attempt-1
        print("your remaining attempt",attempt)
print("your score is",s)
