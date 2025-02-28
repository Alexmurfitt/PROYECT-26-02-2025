from src.mysql_connector import ejecutar_consulta

query = "SELECT * FROM empleados LIMIT 5;"  # Asegúrate de que esta tabla existe en tu base de datos
resultado = ejecutar_consulta(query)

if resultado:
    print("Resultados de la consulta:")
    for fila in resultado:
        print(fila)
else:
    print("No se obtuvieron resultados o hubo un error.")




