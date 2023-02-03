# Q1. Write apython script to reverse a Number ?
x=int(input("Enter a Number :"))
rev=0
while x>0:
    dig=x%10
    rev=rev*10+dig
    x=x//10
print('Reverse Number is :',rev)
