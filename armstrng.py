n=input('enter a number')
l=len(n)
temp=n=int(n)
sum=0
while(n>0):
    sum=sum+((n%10)**l)
    n=n//10
print(sum)
if sum==temp :
    print('number is armstrong')
else :
    print('not an armstrong')
