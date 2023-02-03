# Q7.Write a python script to print whether a given Pair of Numbers are Co-Prime Numbers or not?
num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))
if num1>num2:
    mn=num2
else:
    mn=num1
for a in range(1,mn+1):
    if num1%a==0 and num2%a==0:
        hcf=a
if hcf==1:
    print("Co-Prime Numbers")
else:
    print("Not Co-Prime Numbers")
