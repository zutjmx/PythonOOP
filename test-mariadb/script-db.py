import mariadb

from faker import Faker
fake = Faker('es_MX')

pais = fake.country()
codigo = fake.country_code()
capital = fake.city()

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
sql= "INSERT INTO countries(c_name, country_code, capital) VALUES (?,?,?)"
data = (pais, codigo, capital)
cursor.execute(sql, data)

connection.commit()

# retrieve data
cursor.execute("SELECT c_name, country_code, capital FROM countries")

# print content
#row= cursor.fetchone()
row= cursor.fetchall()
print(*row, sep=' ')

# free resources
cursor.close()
connection.close()
