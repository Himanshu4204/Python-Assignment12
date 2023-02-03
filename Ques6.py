# Q6. Write a python script to print first N Prime Numbers?
x=int(input("Enter Number Range :"))
for i in range(1,x+1):
    if i>1:
        for a in range(2,i):
            if i%a==0:
                break
        else:
            print(i,end=' ')
