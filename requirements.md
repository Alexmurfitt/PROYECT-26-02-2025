**1. Pandas y NumPy**  
Son librerías de Python para el manejo de datos:  
- **Pandas**: Facilita la manipulación y análisis de datos estructurados (tablas). Usa estructuras como `DataFrame` y `Series`.  
- **NumPy**: Proporciona operaciones eficientes con arreglos multidimensionales (`ndarray`), ideales para cálculos numéricos y algebraicos.  

🔹 **Ejemplo:** Pandas se usa para leer y limpiar datos en CSV, mientras que NumPy se usa para cálculos rápidos en matrices.

**DataFrame y Series en Pandas**  

**1. Series**  
Una **Series** en Pandas es una estructura unidimensional similar a una lista o un array de NumPy, donde cada elemento tiene un índice asociado.  

🔹 **Ejemplo:**  
```python
import pandas as pd

serie = pd.Series([10, 20, 30, 40])
print(serie)
```
🔹 **Salida:**  
```
0    10  
1    20  
2    30  
3    40  
dtype: int64
```
Cada valor tiene un índice (0,1,2,3).

---

**2. DataFrame**  
Un **DataFrame** es una estructura **bidimensional** similar a una tabla de Excel o una base de datos. Está compuesto por **columnas de Series** y tiene filas y columnas con etiquetas.  

🔹 **Ejemplo:**  
```python
data = {
    "Nombre": ["Ana", "Carlos", "Juan"],
    "Edad": [25, 30, 22],
    "Ciudad": ["Madrid", "México", "Bogotá"]
}

df = pd.DataFrame(data)
print(df)
```
🔹 **Salida:**  
```
   Nombre  Edad   Ciudad  
0    Ana    25   Madrid  
1  Carlos    30   México  
2   Juan    22   Bogotá  
```

📌 **Diferencias clave:**  
- **Series**: Una columna individual con un solo índice.  
- **DataFrame**: Una tabla completa con múltiples columnas (cada una es una Series).  

**👉 En resumen:**  
- **Series** = Una sola columna de datos.  
- **DataFrame** = Varias columnas organizadas en una tabla.
-------------------------------------------------------------------------------------------------------------------------

ARCHIVOS CSV: Un archivo CSV (valores separados por comas) es un tipo especial de archivo que puede crear o editar en Excel. En lugar de almacenar la información en columnas, los archivos CSV almacenan datos separados por comas. Cuando el texto y los números se guardan en un archivo CSV, es fácil moverlos de un programa a otro.

Un archivo CSV (Comma-Separated Values) es un formato de texto simple utilizado para almacenar datos tabulares, donde cada línea representa una fila y los valores están separados por comas (,) u otros delimitadores como punto y coma (;) o tabulación.
Características clave:

Estructura simple: Filas y columnas organizadas en texto plano.
Delimitadores: Generalmente usa comas, pero pueden emplearse otros separadores.
Ligero y universal: Compatible con múltiples programas (Excel, Google Sheets, bases de datos, Python, etc.).
Sin formato: No admite estilos, fórmulas ni estructuras complejas.

**Ejemplo** :

Nombre,Edad,País  
Juan,25,México  
Ana,30,España  
Carlos,28,Argentina  

En resumen, un archivo CSV es un formato estándar para almacenar y compartir datos estructurados de manera simple y eficiente.

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Una API (Application Programming Interface) es un conjunto de reglas y definiciones que permite que dos sistemas de software se comuniquen entre sí. Funciona como un intermediario que facilita el intercambio de datos y funciones sin que las aplicaciones involucradas necesiten conocer los detalles internos de cada una.
Características clave:

Interfaz definida: Especifica cómo se hacen las solicitudes y qué respuestas se pueden esperar.
Estandarización: Puede seguir protocolos como REST, SOAP o GraphQL.
Seguridad: Puede requerir autenticación mediante claves API, tokens o OAuth.
Independencia: Permite que diferentes tecnologías y plataformas interactúen sin problemas.

**Ejemplo práctico:**

Cuando usas una app de clima en tu móvil, esta consulta una API de un servicio meteorológico, que devuelve los datos actualizados del clima sin que la app necesite recopilar la información directamente.

En resumen, una API es el puente que permite que diferentes aplicaciones intercambien información de manera estructurada y segura.


![image](https://github.com/user-attachments/assets/05b3ac1e-c45f-4a0d-bbc0-efb3a936dd6d)
![image](https://github.com/user-attachments/assets/a7bff1a5-2f4b-4eaa-a9db-36330aa7680e)


-------------------------------------------------------

**2. Matplotlib y Seaborn**  
Son librerías de visualización de datos:  
- **Matplotlib**: Crea gráficos personalizables (barras, líneas, dispersión, etc.).  
- **Seaborn**: Extiende Matplotlib con gráficos más estéticos y fáciles de usar, optimizados para análisis estadístico.  

🔹 **Ejemplo:** Usas Matplotlib para crear gráficos básicos y Seaborn para visualizaciones más avanzadas y estilizadas.  

---

**3. mysql-connector-python**  
Es una librería que permite conectar Python con bases de datos **MySQL**.  
- Permite ejecutar consultas SQL (`SELECT`, `INSERT`, `UPDATE`, etc.).  
- Facilita la interacción entre Python y MySQL sin necesidad de herramientas externas.  

🔹 **Ejemplo:** Se usa para extraer datos de una base de datos MySQL y analizarlos en Pandas.  

---

**4. gspread y oauth2client**  
Son librerías para trabajar con **Google Sheets** desde Python:  
- **gspread**: Permite leer, escribir y actualizar hojas de cálculo de Google Sheets.  
- **oauth2client**: Gestiona la autenticación segura con OAuth 2.0 para acceder a Google Sheets.  

🔹 **Ejemplo:** Se usa para automatizar la actualización de datos en Google Sheets desde un script en Python.  

---

📌 **En resumen:**  
- **Pandas y NumPy** → Manipulación y análisis de datos.  
- **Matplotlib y Seaborn** → Visualización de datos.  
- **mysql-connector-python** → Conexión con bases de datos MySQL.  
- **gspread y oauth2client** → Interacción con Google Sheets.

