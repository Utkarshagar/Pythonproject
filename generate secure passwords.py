import random
p=int(input('''entre 1 for generating 8 character long password
entre 2 for generating 9 character password
entre 3 for generating 10 character password
entre 4 for generating 11 charcter password
entre 5 for generating 12 digit password: '''))
if p==1:
    sequence=''
    for i in range(8):
        r=random.randint(65,122)
        sequence+=chr(r)
    print('your 8 character sequence passwod is: ',sequence)
elif p==2:
    sequence=''
    for i in range(9):
        r=random.randint(65,122)
        sequence+=chr(r)
    print('your 9 character sequence passwod is: ',sequence)
elif p==3:
    sequence=''
    for i in range(10):
        r=random.randint(65,122)
        sequence+=chr(r)
    print('your 10 character sequence passwod is: ',sequence)
elif p==4:
    sequence=''
    for i in range(11):
        r=random.randint(65,122)
        sequence+=chr(r)
    print('your 11 character sequence passwod is: ',sequence)
elif p==5:
    sequence=''
    for i in range(12):
        r=random.randint(65,122)
        sequence+=chr(r)
    print('your 12 character sequence passwod is: ',sequence)