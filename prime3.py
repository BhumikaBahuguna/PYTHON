n=int(input('enter a number'))
flag=0
for i in range(2,int(n**0.5)):
    if n%i==0 :
        flag=1
        break
if flag:
    print("not a prime number")
else :
    print("prime number")
print("steps::")
print(i)
