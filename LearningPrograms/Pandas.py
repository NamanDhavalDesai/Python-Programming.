import pandas as pd
#Series.
_dataset = {
    'Subjects': ["EM4", "OS", "COA"],
    'Marks': [19, 18, 20]
}
a=pd.Series(_dataset)
print(a)
#DataFrame.
df1=pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
    },index=[0,1,2,3],
)
print(df1)
df2 = pd.DataFrame( 
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
    },index=[4,5,6,7],
)
print(df2)
#Combination.
con=[df1,df2]
result=pd.concat(con)
print(result)
#Merging.
A= pd.DataFrame({
        'id':[1,2,3,4,5],
        'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'subject_id':['sub1','sub2','sub4','sub6','sub5']})
print(A)
B= pd.DataFrame({
        'id':[1,2,3,4,5],
        'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print(B)
print(pd.merge(A,B,on='id'))
#Filtering.
df = pd.read_csv("C:/Users/naman/Desktop/NRX07/Programing/Python/Python Programs/nba.csv")
print(df)
print("\n After filter \n")
f=df.filter(["Name", "College", "Salary"])
print(f)
#Indexing.
data = pd.read_csv("nba.csv", index_col ="Name")
i = data["Age"]
print(i)