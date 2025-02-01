import mariadb

# connection parameters
conn_params= {
    "user" : "zutjmx",
    "password" : "sistemas",
    "host" : "192.168.1.245",
    "database" : "bd-processlog"
}

# Establish a connection
connection= mariadb.connect(**conn_params)

cursor= connection.cursor()

# Populate countries table  with some data
# cursor.execute("INSERT INTO countries(c_name, country_code, capital) VALUES (?,?,?)",
#                ("Germany", "GER", "Berlin"))

# connection.commit()

# retrieve data
cursor.execute("SELECT c_name, country_code, capital FROM countries")

# print content
#row= cursor.fetchone()
row= cursor.fetchall()
print(*row, sep=' ')

# free resources
cursor.close()
connection.close()
