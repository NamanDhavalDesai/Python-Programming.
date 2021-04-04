#Simple Calculator.
def add1(a,b):
    "Function to add"
    return [a+b]
def sub1(a,b):
    "Function to subtract"
    return [a-b]
def mul1(a,b):
    "Function to multiply"
    return [a*b]
def div1(a,b):
    "Function to divide"
    return [a/b]
def exp1(a,b):
    "Function to exponenciate"
    return [a**b]
count=1
while count==1:
    print("Simple Calculator:");
    print("Enter 1 to add.");
    print("Enter 2 to subtract.");
    print("Enter 3 to multiply.");
    print("Enter 4 to divide.");
    print("Enter 5 to exponenciate.");
    print("Enter 0 to quit.");
    ch=int(input("Enter the choice: "));
    if ch==0:
        print("Exiting the calculator.");
        break;
    elif ch==1:
        num1=int(input("Enter the number 1: "));
        num2=int(input("Enter the number 2: "));
        print("The answer is :",float(add1(num1,num2)[0]));
    elif ch==2:
        num1=int(input("Enter the number 1: "));
        num2=int(input("Enter the number 2: "));
        print("The answer is :",float(sub1(num1,num2)[0]));
    elif ch==3:
        num1=int(input("Enter the number 1: "));
        num2=int(input("Enter the number 2: "));
        print("The answer is :",float(mul1(num1,num2)[0]));
    elif ch==4:
        num1=int(input("Enter the number 1: "));
        num2=int(input("Enter the number 2: "));
        print("The answer is :",float(div1(num1,num2)[0]));
    elif ch==5:
        num1=int(input("Enter the number 1: "));
        num2=int(input("Enter the number 2: "));
        print("The answer is :",float(exp1(num1,num2)[0]));
    else:
        print("Choose Properly");

#Using lambda and map Function.
c=[100,99,87,76,69]
F1=list(map(lambda x:float((x-32)*(5/9)),c))
print(F1)
a=[1,2,3,4,5]
b=[10,20,30,40,50]
c=[100,200,300,400,500]
F2=list(map(lambda x,y,z:x+y+z,a,b,c))
print(F2)
#Using the filter function with the lambda function.
F3=list(filter(lambda x:x%2==0,F2))
F4=list(filter(lambda x:x%2,F2))
print(F3)
print(F4)
#Uisng the reduce and lamda function and range.
x=6
import functools
print(functools.reduce(lambda x,y:x*y,range(1,x)))