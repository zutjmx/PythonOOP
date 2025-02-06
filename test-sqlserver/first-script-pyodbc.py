"""
Connects to a SQL database using pyodbc
"""

import pyodbc

server = 'HUAWEI-ZUTJMX'
database = 'AdventureWorks2022'
username = 'sa'
password = 'sistemas'

# Create a connection string
connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Create a connection
conn = pyodbc.connect(connectionString)
# Create a cursor
cursor = conn.cursor()
# Execute a query
sql = 'SELECT BusinessEntityID, PersonType, FirstName, MiddleName, LastName FROM Person.Person'
cursor.execute(sql)
# Fetch the results
rows = cursor.fetchall()
# Print the results
for row in rows:
    print(row)

conn.close()
