import mysql.connector

def conectar_mysql():
    """Conecta a MySQL y devuelve la conexión."""
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",  # Usa 127.0.0.1 en lugar de localhost
            user="root",
            password="student2025",  # Usa la contraseña que hayas establecido
            database="test_db"  # Asegúrate de usar test_db, la base de datos correcta
        )
        print("✅ Conectado a MySQL.")
        return conn
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

def ejecutar_consulta(query):
    """Ejecuta una consulta en MySQL y devuelve los resultados."""
    conn = conectar_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        conn.close()
        return resultado
    return None

# Realiza la consulta en Python
query = "SELECT * FROM empleados LIMIT 5;"  # Cambia el nombre de la tabla si es necesario
resultado = ejecutar_consulta(query)

if resultado:
    print("Resultados de la consulta:")
    for fila in resultado:
        print(fila)
else:
    print("No se obtuvieron resultados.")



