'''
Write a  Python  program to implement Range, Set and STRING  Functions. 

a) Create range of first 10 integers and Create list of odd integers 
from 3 to 15 using range. 

b) Create integer set from list and character set. Perform following 
functions on the same: add(), update(),discard(), remove(), 
pop(), union(), intersection(), difference(), symmetric_difference() 
and clear(). 

c) Print elements of string using slice operator. 

d) Print first and last character of a String. 

e) Display string thrice. 

f) Use replace(), lower(), count(), capitalize(), len(), 
upper(), title(), find(), join(), split(), isalnum(), 
isalpha(), isdigit(), islower() and isupper() functions. 
'''

print("Printing the first 10 integers:")
list1=[]
for i in range(0,10):
	list1.append(i)
print(list1)

print('\n')
print("Printing odd numbers :")
odd=[]
for i in range(3,15,2):
	odd.append(i)
print(odd)

print("\n")
inte_set={1,2,3,4,5,6,89,56,"hello","world","all","hey"}
#char_set={}
print(inte_set)
#print(char_set)

print('\n')
print("Adding new element")
inte_set.add(72)
print(inte_set)

print("\n")
print("Updating the Set :")
inte_set2={12,34,54}
inte_set.update(inte_set2)
print(inte_set)


print("\n")
print("Discarding the set")
inte_set.discard(12)
print(inte_set)

print("\n")
print("Removing the set")
inte_set.remove(34)
print(inte_set)

print("\n")
print("Poping the element from set")
inte_set.pop()
print(inte_set)

print('\n')
print("Printing set 1",inte_set)
print("Printing set 2",inte_set2)
print('\n')
print("Printing Uninon of Sets :",inte_set.union(inte_set2))
print("Printing Intesection of Sets",inte_set.intersection(inte_set2))
print("Printing the difference of two Sets",inte_set2-inte_set)
print("Symmetric difference of two sets :",(inte_set-inte_set2).union(inte_set2-inte_set))
print("Clearing the set :",inte_set.clear)


print("\n")
str1="Hello World"
print("The string is :",str1)
print("Use of slice operation",str1[0:5])
print("Printing the First Character :",str1[0])
print("Printing the last Character :",str1[-1])
print("Printing the string thrice :",(str1*3))

print("using the replace function:",str1.replace("World","Everyone"))

print("To lower function",str1.lower())
print("To upper function",str1.upper())
print("counting no. of occurence of letter E  :",str1.count("e"))
print("use of capatilize function :",str1.capitalize())
print("Length of String",len(str1))
print("Title of String :",str1.title())
print("Finding the letter i  :",str1.find('i'))
print("Use of split functino",str1.split(" "))
print("Islower function :",str1.islower())
print("isupper function :",str1.isupper())
print("isdigit function :",str1.isdigit())
print("isaplha function :",str1.isalpha())
print("isalnum function :",str1.isalnum())


print('\n')
tup=("Python", "is" ,"a" ,"language")
print(tup)
print("Use of Join function: ")
print(" ".join(tup,tup))