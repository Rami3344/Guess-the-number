from random import *
def clientInp():
    global n
    ok = False
    while(ok==False):
        n=int(input("type your number :"))
        ok = (n>0) and (n!="") and(randomNum(n))


nb = randint(1,10)

def randomNum(x):
    ok = False
    while(ok==False):
        if(x!=nb):
            print("guess the number again")
            return False
        else:
            print("good job u made it ! , The number is : " ,str(nb))
            return True
    
clientInp()
