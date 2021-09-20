from sys import exit
#if n is even next number is n/2
#if n is odd next number is 3n+1
def collatz(y):
    if(y%2==0):
        y=y//2
    else:
        y=(3*y)+1
    return y

def collseqlen(i):
    leng=1
    coll=list()
    coll.append(i)
    while(i!=1):
        i=collatz(i)
        coll.append(i)
        leng+=1
        
    for k in coll:
        if k not in coll:
            coll[k]=len(coll)-coll.index(k)
    return (leng)

def collseq(x):
    collx=list()
    while(x!=1):
        collx.append(x)
        x=collatz(x)
    collx.append(1)
    print("Collatz Sequence of ",x)
    for j in range (0,len(collx)):
        print(collx[j])
    print("Length of the Collatz Sequence of number ",x," is ",len(collx))
    
def findlongestseq():
    max=1
    for j in range(1,1000000):
        n=collseqlen(j)
        if(n>max):
            max=n
            longestnum=j
    print("Longest Collatz Sequence is made using ",longestnum)
    print("Length is ",max)
    z=input("Would you like to see the sequence? (Yes/No): ")
    if(z=="Yes"):
        collseq(max)
    else:
        exit()

print("Welcome to Collatz Sequence Solver!\n")
m=int(input("1. Make a sequence\n2. Find the longest sequence\n3. Exit\n"))
if(m==1):
    num=int(input("Enter the initial number: "))
    collseq(num)
elif(m==2):
    findlongestseq()
elif(m==3):
    exit()

