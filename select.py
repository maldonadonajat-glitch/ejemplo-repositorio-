import mysql.connector

# conectar a la base de datos
conexion = mysql.connector.connect(
    host="localhost", user="root", password="admin", database="facturacion_db"
)
cursor = conexion.cursor()
criterio = input("Ingrese el criterio de búsqueda ")
query = f"SELECT * FROM articulos WHERE descripcion LIKE '%{criterio}%'"

# ejecutar SELECT 
cursor.execute(query)
resultado = cursor.fetchall()

# mostrar los datos
for fila in resultado:
    print(fila)

# cerrar conexión
conexion.close()