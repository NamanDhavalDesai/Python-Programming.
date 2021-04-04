#Zero division error.
try:
    a=3/0
except ZeroDivisionError:
    print("Dividing by 0 is not possible.")
#Index error
try:
    a=[1,2,3,4]
    print(a[4])
except IndexError:
    print("Index out of bounds.")
#Module error
try:
    import alop
except ImportError:
    print("Module not found.")
#Key error.
try:
    a={'a':1,'b':2}
    print(a['c'])
except KeyError:
    print("The key c is not present.")
#Value error.
try:
    a='one'
    b=int(a)
except ValueError:
    print("Can not convert integer to string.")

    
