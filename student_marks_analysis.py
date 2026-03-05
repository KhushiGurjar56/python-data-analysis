import pandas as pd
d1={'name':['khushi','anshika','muskan','sameeksha'],
    'courses':['BCA','BCA','MBA','BBA'],
    'marks':[89,87,78,56]}
df=pd.DataFrame(d1)
print("STUDENT DATA :")
print(df)
print("\nAverage marks :",df['marks'].mean())
print("HIGHEST MARKS :",df['marks'].max())
