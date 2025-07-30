import sqlite3

# Se importa Faker
from faker import Faker
fake = Faker('es_MX')

with sqlite3.connect("../Datos/mi_base.db") as conexion:
    cursor = conexion.cursor()
    print("Base de datos abierta")

    # Write the SQL command to create the Students table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER,
        email TEXT
    );
    '''

    # Execute the SQL command
    cursor.execute(create_table_query)

    # Insert a record into the Students table
    insert_query = '''
    INSERT INTO Estudiantes (nombre, edad, email) 
    VALUES (?, ?, ?);
    '''

    data_estudiantes = [
        (fake.name(), fake.random_int(min=18, max=30), fake.email())
        for _ in range(10)
    ]
    
    cursor.executemany(insert_query, data_estudiantes)


    # Commit the changes
    conexion.commit()

    # Print a confirmation message
    print("Records inserted successfully!")

cursor.execute("SELECT * FROM Estudiantes")
rows = cursor.fetchall()
print("Datos de la tabla Estudiantes:")
for row in rows:
    print(row)
    
conexion.close()
    