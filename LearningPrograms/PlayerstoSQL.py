import csv
import MySQLdb as mysql
mydb=mysql.connect(
    host="localhost",
    user="root",
    password="Nrx07CR7."
)
mycursor=mydb.cursor()
mycursor.execute("use mini;")
file = open("players.csv", encoding='utf-8')
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    if row[3].find("'") > 0:
        row[3].replace("'"," ")
    if row[4].find("'") > 0:
        row[4].replace("'"," ")
    if row[5].find("'") > 0:
        row[5].replace("'"," ")
    if row[6].find("'") > 0:
        row[6].replace("'"," ")
    val=(int(row[0]),int(row[1]),row[2],row[3],row[4],row[5],row[6],row[7])
    print(val)
    query="insert into players (hash_,rating,position,name,club,league,country,skillboost) values (%s,%s,%s,%s,%s,%s,%s,%s);"
    mycursor.execute (query,val)
    mydb.commit()
file.close()