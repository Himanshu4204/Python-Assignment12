# Q9. Write a python script to calculate LCM of Two Numbers ?
a=int(input("Enter first Number :"))
b=int(input("Enter Second Number :"))
max=max(a,b)
while True:
    if max%a==0 and max%b==0:
        break
    max=max+1
print(f"LCM is {max}")
