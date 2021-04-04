#Creating a list of integers.
L1=[1,2,3,4,5,6,7,8,9]
#Creating a list of mixed data types, nested lists and duplicate items.
L2=[1,20,"Hello",True,3.14,2+4j,[1,2,3,4,5],('a','b','c'),1,True,20,30]
#Simple indexing.
print(L1[1]) #Prints the 2nd element.
print(L1[1:4]) #Prints the second to fourth element.
print(L1[4:-2]) #Prints from the fouth to the second last elements.
#Nested indexing.
print(L2[6][1:3]) #Prints the second and third elements from the list at the 7th element of the list.
#Lists are mutable.
L2[-1]=1
print(L2[-1])
#Appending list.
L3=[1,2,3]
L3.append(4)
L3.append(5)
print(L3)
#Extending the list.
L3.extend(['a','b'])
print(L3)
#Inserting in the list. 
L2.insert(-1, L3)
print(L2)
#Removing from the list.
L3.remove('a')
print(L3)
#Popping from the list.
L3.pop()
print(L3)
#Clearing the list.
L1.clear()
print(L1)
#Indexing duplicate values and expecting to get the index of the first occurance.
print(L2.index(1))
#Counting the number of duplicate elements in the list.
print(L2)
print(L2.count(1)) #It counted the element 1 from the nested lists too.
#Sorting a list.
L3.append(0)
L3.sort()
print(L3)
#Reversing a list.
L3.reverse()
print(L3)
#Coppying a list.
L1=L3.copy()
T1=('January','February','March','April','May','June','July','August','September','October','Novemeber','December')
print(T1)
#Converting list to tuple.
T2=tuple(L1)
print(T2)
#All function.
print(all(T2))
#Any functon.
print(any(T2))
#Length of tuple.
print(len(T2))
#Maximum of the tuple.
print(max(T2))
#Minimum of the tuple.
print(min(T2))
#Printing the sorted tuple.
print(sorted(T2))
#Taking the summation of the tuple.
print(sum(T2))
#Tuples are not mutable.
#T2[5]=4
#Creating a dictionary of fruits.
Fruits={'apple':'red','banana':'yellow','grapes':'green','strawberry':'red','pineapple':'yellow','orange':'orange'};
print(Fruits)
#Craeting another dictionary using dict.
F1=dict([('apple', 'red'), ('banana', 'yellow'), ('grapes', 'green'), ('strawberry', 'red'), ('pineapple', 'yellow'), ('orange', 'orange')])
#Popping an element from the list.
F1.pop('pineapple')
print(F1)
#Popping an item from the list. The last one namely.
F1.popitem();
print(F1)
#Clearing the entire list.
F1.clear()
print(F1)
#Getting an particular value form the dictionary using the key.
print(Fruits.get('apple'))
#Taking all the keys.
print(Fruits.keys())
#Taking all the vlaues.
print(Fruits.values())
#Updating the dictionary by adding and modifying two values.
Fruits.update({'dragonfruit':'pink','orange':'Color_orange'})
print(Fruits)
#Using fromkeys to set the value of all keys as the same value.
marks={}.fromkeys(['COA','OS','CNND','AT','EMIV','PY'],80)
print(marks)