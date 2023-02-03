# Q10. Write a python script to calculate HCF of Two Numbers?
a=int(input("Enter first Number :"))
b=int(input("Enter Second Number :"))
min=min(a,b)
hcf=0
for i in range(1,min+1):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf)