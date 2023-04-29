import random
n=int(input("enter 1 for 4 digit otp and 2 for 6 digit otp "))
if(n==4):
    otp=''
    for i in range(4):
        a=str(random.randint(0,9))
        otp=otp+a
    print(otp)
else:
    otp=''
    for i in range(6):
        a=str(random.randint(0,9))
        otp=otp+a
    print(otp)