from src.mysql_connector import ejecutar_consulta

query = "SELECT * FROM empleados;"
resultado = ejecutar_consulta(query)

print("📌 Resultado de la consulta:")
for fila in resultado:
    print(fila)



