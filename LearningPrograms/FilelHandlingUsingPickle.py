import pickle
a = ["A", "B", "C"]
f_name = "file1.txt"
f1= open(f_name, 'wb')
pickle.dump(a,f1)
f1.close()
f1= open(f_name, 'rb')
b=pickle.load(f1)
print(b)
print(a==b)


file = open('naman.txt','w')
file.write("This is Naman's file")
file.close()
f = open("naman.txt", "r")
print(f.read())



