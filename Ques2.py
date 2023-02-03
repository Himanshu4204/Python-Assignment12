# Q2. Write a python script to check whether a given number is prime or not ?
x=int(input("Enter a Number :"))
if x>1:
    for a in range(2,int(x/2)+1):
        if x%a==0:
            print(x,"is not a prime number")
            break
    else:
        print(x," is a prime Number")
else:
    print(x,"is Not a prime Number")
