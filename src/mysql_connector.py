import mysql.connector

def conectar_mysql():
    """Conecta a una base de datos MySQL y devuelve la conexión."""
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
    """Ejecuta una consulta SQL y devuelve los resultados."""
    conn = conectar_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        conn.close()
        return resultado
    return None

