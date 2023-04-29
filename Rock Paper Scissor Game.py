import random
print('''rules for the game:-
      1.('Rock beats Scissor')
      2.('Paper beats Rock')
      3.('Scissor beats Paper')''')
ls=random.choice(['Rock','Paper','Scissor'])
s=input('entre your decision: ')
if s=='Rock' and ls=='Scissor' or s=='Paper' and ls=='Rock' or s=='Scissor' and ls=='Paper':
    print('user win')
    print('you decision is',s)
    print('computer decision is',ls)
elif s==ls:
    print('Tie game')
    print('you decision is',s)
    print('computer decision is',ls)
else:
    print('computer win')
    print('you decision is',s)
    print('computer decision is',ls)

   
    a=input('entre 1 for restart the game and 0 for exit the game',)
    while a:
        ls=random.choice(['Rock','Paper','Scissor'])
        s=input('entre your decision: ')
        if s=='Rock' and ls=='Scissor' or s=='Paper' and ls=='Rock' or s=='Scissor' and ls=='Paper':
            print('user win')
            print('you decision is',s)
            print('computer decision is',ls)
        elif s==ls:
            print('Tie game')
            print('you decision is',s)
            print('computer decision is',ls)    
        else:
            print('computer win')
            print('you decision is',s)
            print('computer decision is',ls)
    
          
    