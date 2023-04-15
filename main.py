import pyodbc
import pandas as pd

# insert data from csv file into dataframe.
df = pd.read_csv("hired_employees.csv", names=['id','name','datetime','department_id','job_id'])

# Connection to SQL SERVER with windows authentication
conn_str = ("Driver={SQL Server};"
            "Server=DESKTOP-GKE34FR;"
            "Database=Globant;"
            "Trusted_Connection=yes;")
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


# Insert Dataframe into SQL Server:
for index, row in df.iterrows():
     cursor.execute("INSERT INTO hired_employees (id,name,datetime,department_id,job_id) values(?,?,?,?,?)", row.id, row.name, row.datetime, row.department_id, row.job_id)
conn.commit()
cursor.close()

# Quisas agregar un try except para que en caso que ocurra un error poner ROOLBACK