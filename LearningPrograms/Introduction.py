#input value.
a=input("Input please number 1\n")
b=input("Input please number 2\n")
#Converting to float.
a=float(a)
b=float(b)
#Stating type of the values accepted.
print("type of number 1 is ",type(a))
print("type of number 2 is ",type(b))
#Computing operations.
print("The sum is ",(a+b))
print("The difference is ",(a-b))
print("The product is ",(a*b))
print("The quotient is ",(a/b))
print("The modulus is ",(a%b))
print("The modulus with loss of decimal spce is ",(a//b))
print("The powered value is ",(int(a)**int(b)))
#Converting to int.
a=int(a)
b=int(b)
#Stating type of the values accepted.
print("type of number 1 is ",type(a))
print("type of number 2 is ",type(b))
#Computing bit-wise opertions.
print("The bitwise and operator is ",(a&b))
print("The bitwise or operator is ",(a|b))
print("The bitwise exor operator is ",(a^b))
print("The bitwise not operator is ",(~a)," ",(~b))
print("The bitwise rightshift operator is ",(a>>b))
print("The bitwise leftshift operator is ",(a<<b))
c=input("Input please complex number 1\n")
d=input("Input please complex number 2\n")
#Converting to complex number.
c=complex(c)
d=complex(d)
#Stating type of the values accepted.
print("type of number 1 is ",type(c))
print("type of number 2 is ",type(d))
#Computing complex operations
print("The sum of the complex number is ", (c+d))
#Stating type of the values accepted.
print("type of number 1 is ",type(a))
print("type of number 2 is ",type(b))
#Converting and printing numbers into octal, binary and hexadecimal.
print("The octal convertion is ",oct(a),oct(b))
print("The binary convertion is ",bin(a),bin(b))
print("The hexadecimal convertion is ",hex(a),hex(b))
