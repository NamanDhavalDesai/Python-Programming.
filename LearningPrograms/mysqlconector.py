import MySQLdb as mysql
mydb=mysql.connect(
    host="localhost",
    user="root",
    password="Nrx07CR7."
)
mycursor=mydb.cursor()
mycursor.execute("create database if not exists pyEXP12;")
mycursor.execute("use pyEXP12;")
mycursor.execute("create table if not exists rollcall(name varchar(10) primary key, rollno int(2));")


query="insert into rollcall (name,rollno) values (%s,%s);"
val=("paa",16)
mycursor.execute (query,val)
mydb.commit()

mycursor.execute("delete from rollcall where rollno=10;")
mydb.commit()

mycursor.execute("select rollno from rollcall")
res=mycursor.fetchall()
for x in res:
    print(type(x[0]))