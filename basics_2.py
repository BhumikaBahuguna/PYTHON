#odd-even
num=int(input("enter a number:"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")


#odd-even
num=int(input("enter a number:"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
if(num1>num2):
    print("largest is:",num1)
else :
    print("largest is:",num2)


#IF ELIF
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>b and a>c):
    print("largest is:",a)
elif(b>a and b>c):
    print("largest is:",b)
else:
    print("largest is:",c)

p=float(input("enter percentage:"))
if(p>90 and p<=100):
    print("grade:A")
elif(p>80 and p<=90):
     print("grade:B")
elif(p>60 and p<=80):
    print("grade:C")
elif(p<60):
     print("grade:D")
else:
    print("invalid input")


u=int(input("enter units:"))
if(u<=100):
    print("no charge")
elif(u>100 and u<=200):
    x=(u-100)*5;
    print("charge is:",x)
else:
    y=u-200;
    print("charge is:",(u-100)*5+(u-200)*10)


alpha=['a','b','c','d','e']
for x in alpha:
    print(x)

for x in range(3,10):
    print(x)

for x in range(3,10,2):
    print(x)

for x in range(10,0,-1):
    print(x)
