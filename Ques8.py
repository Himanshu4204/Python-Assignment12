# Q8. Write a python script to print first N terms of a Fibonacci Series ?
n=int(input("Enter a Number :"))
x=0
y=1
z=0
if n<=0:
    print("Enter a valid Number")
elif n==1:
    print(x)
else:
    while z<n:
        print(x,end=' ')
        sum=x+y
        x=y
        y=sum
        z+=1




