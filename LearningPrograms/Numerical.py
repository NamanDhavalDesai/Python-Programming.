a=int(input("Input please the number: "))
b=a
l=0
s=0
while b>0:
    b=b//10
    l=l+1
b=a
while b>0:
    s=s+((b%10)**l)
    b=b//10
if a==s:
    print(a," is an armstrong number")
else:
    print(a," is not an armstrong number")
#-------------------------------------------------------------------------
a=int(input("Input please the number: "))
s=1
if a<0:
    print("Factorial is not possible")
elif a==0:
    print("The factorial of the number is 1")
else:
    while a>0:
        s=s*(a)
        a=a-1
    print("The factorial is ",s)
#-------------------------------------------------------------------------
a=int(input("Please enter the year: "))
if a%4==0:
    if a%400==0:
        print("It is a leap year")
    else:
        print("It is not a leap year")
else:
    print("It is not a leap year")
#-------------------------------------------------------------------------
a=int(input("Input please the number of rows: "))
c=0
e=0
lo=a
while a!=c:
    e=0
    while lo-e-1>0:
        print(" ",end="")
        e=e+1
    d=0
    while d<=c:
        ii=1
        s1=1
        while ii<=c:
            s1=s1*ii
            ii=ii+1
        ii=1
        s2=1
        while ii<=d:
            s2=s2*ii
            ii=ii+1
        ii=1
        s3=1
        while ii<=c-d:
            s3=s3*ii
            ii=ii+1
        print(int(s1/(s2*s3)),end="")
        print(" ",end="")
        d=d+1
    print("\n")
    c=c+1
    lo=lo-1
#-------------------------------------------------------------------------
a=int(input("Input please the number of rows: "))
for l1 in range(0,a):
    for l2 in range(a-l1):
        print(" ",end="")
    for l3 in range(0,l1+1):
        s1=1
        s2=1
        s3=1
        for l4 in range(1,l1+1):
            s1=s1*l4
        for l4 in range(1,l3+1):
            s2=s2*l4
        for l4 in range(1,l1-l3+1):
            s3=s3*l4
        print(int(s1/(s2*s3)),end="")
        print(" ",end="")
    print("\n")