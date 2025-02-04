import mariadb

# connection parameters
conn_params= {
    "user" : "zutjmx",
    "password" : "sistemas",
    "host" : "192.168.1.199",
    "database" : "db_usuarios_springboot"
}

# Establish a connection
connection= mariadb.connect(**conn_params)

cursor= connection.cursor()


# retrieve data
cursor.execute("SELECT nombre, paterno, materno FROM personas ORDER BY id")

# print content
#row= cursor.fetchone()
row= cursor.fetchall()
print(*row, sep=' ')

# free resources
cursor.close()
connection.close()
