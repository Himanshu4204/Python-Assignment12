# Q5. Write a python script to find next Prime Number of a given Number ?
x=int(input("Enter a Number :"))
a=x+1
while True:
    if a>1:
        for b in range(2,int(a/2)+1):
            if a%b==0:
                break
        else:
            print(" Next Prime Number is:",a)
            break
        a+=1





   
