# Q4. Write a python program to print all prime numbers between two given numbers(both values inclusive)?
x=int(input("Enter starting Value:"))
y=int(input("Enter ending Value :"))
print(f"Prime Number between {x} and {y} is :")
for a in range(x,y+1):
    if a>1:
        for b in range(2,int(a)):
            if a%b==0:
                break
        else:
            print(a,end=' ')


