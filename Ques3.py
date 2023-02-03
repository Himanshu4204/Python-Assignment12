# Q3. Write a python script to print all prine numbers under 100?
for a in range(1,101):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                break
        else:
            print(a,end=' ')

