"""
Connects to a SQL database using pymssql
"""

import pymssql

conn = pymssql.connect(
    server='HUAWEI-ZUTJMX', 
    user='sa', 
    password='sistemas', 
    database='AdventureWorks2022'
)

cursor = conn.cursor()
sql = 'SELECT BusinessEntityID, PersonType, FirstName, MiddleName, LastName FROM Person.Person'
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
