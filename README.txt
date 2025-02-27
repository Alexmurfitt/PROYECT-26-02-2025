GUIA PARA PROYECTO

📌 1. Descripción del Proyecto
🎯 Objetivo

Crear un programa en Python que permita: 

✅ Cargar y limpiar datos desde CSV y Google Sheets
✅ Explorar y visualizar datos con Pandas y Matplotlib
✅ Conectar a una base de datos MySQL y realizar consultas
✅ Generar reportes en Google Looker Studio usando datos estructurados
✅ Usar GitHub para trabajo en equipo

¿Qué aprenderán con este proyecto? 
✔️ Manipulación de datos con Pandas
✔️ Consultas SQL con MySQL
✔️ Integración con Google Sheets API
✔️ Creación de reportes con Looker Studio
✔️ Trabajo colaborativo con GitHub
📌 2. Instalación de Python y Librerías

Antes de empezar, instalen las librerías necesarias:

pip install pandas numpy matplotlib seaborn mysql-connector-python gspread oauth2client

Esto instalará:

    Pandas y NumPy → Para manipulación de datos
    Matplotlib y Seaborn → Para visualización
    mysql-connector-python → Para conectarse a MySQL
    gspread y oauth2client → Para trabajar con Google Sheets

📌 3. Organización del Proyecto

📂 analisis-datos-python/
   ├── 📜 README.md (Documentación del proyecto)
   ├── 📜 requirements.txt (Lista de librerías necesarias)
   ├── 📂 data/ (Archivos CSV o Google Sheets)
   ├── 📂 src/ (Código fuente del programa)
   │     ├── 📜 main.py (Ejecuta la aplicación principal)
     │ ├── 📜 data_loader.py (Carga de datos desde CSV o Google Sheets)
     │ ├── 📜 mysql_connector.py (Conexión y consultas a MySQL)
     │ ├── 📜 analysis.py (Exploración y limpieza de datos)
     │ ├── 📜 visualization.py (Gráficos y reportes)

📌 4. Desarrollo Paso a Paso
🔹 1️⃣ Carga de Datos desde CSV o Google Sheets (data_loader.py)
📂 Opción 1: Cargar un archivo CSV

import pandas as pd

def cargar_datos_csv(ruta_archivo):
    """Carga datos desde un archivo CSV y devuelve un DataFrame."""
    try:
        df = pd.read_csv(ruta_archivo)
        print("✅ Datos cargados correctamente desde CSV.\n")
        return df
    except Exception as e:
        print(f"❌ Error al cargar el archivo CSV: {e}")
        return None

📌 Para probarlo:

df = cargar_datos_csv("data/datos.csv")
print(df.head())

📂 Opción 2: Cargar datos desde Google Sheets

Para acceder a Google Sheets, primero deben habilitar la API de Google Sheets y obtener un archivo JSON con las credenciales.
🔹 Configurar Google Sheets API

    Ir a Google Cloud Console
    Crear un nuevo proyecto
    Habilitar la API de Google Sheets
    Crear credenciales (OAuth 2.0 o clave de servicio)
    Descargar el archivo JSON con las credenciales y guardarlo en config/credenciales.json

🔹 Código para cargar datos de Google Sheets

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def cargar_datos_sheets(sheet_url):
    """Carga datos desde Google Sheets en un DataFrame."""
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("config/credenciales.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_url(sheet_url).sheet1
        data = sheet.get_all_records()
        df = pd.DataFrame(data)
        print("✅ Datos cargados correctamente desde Google Sheets.\n")
        return df
    except Exception as e:
        print(f"❌ Error al cargar datos desde Google Sheets: {e}")
        return None

📌 Para probarlo:

df = cargar_datos_sheets("https://docs.google.com/spreadsheets/d/ID_DE_TU_SHEET")
print(df.head())

🔹 2️⃣ Conexión a MySQL y Ejecución de Consultas (mysql_connector.py)

Configurar MySQL para conectarse a una base de datos.

import mysql.connector

def conectar_mysql():
    """Conecta a una base de datos MySQL y devuelve la conexión."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="tu_base_de_datos"
        )
        print("✅ Conectado a MySQL.")
        return conn
    except Exception as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

📌 Ejecutar una consulta simple

def ejecutar_consulta(query):
    conn = conectar_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        conn.close()
        return resultado

🔹 3️⃣ Exploración y Limpieza de Datos (analysis.py)

def explorar_datos(df):
    """Muestra información y estadísticas básicas."""
    print(df.info())
    print("\nEstadísticas:")
    print(df.describe())

🔹 4️⃣ Visualización de Datos (visualization.py)

import matplotlib.pyplot as plt
import seaborn as sns

def graficar_histograma(df, columna):
    """Genera un histograma de una columna numérica."""
    plt.figure(figsize=(6, 4))
    sns.histplot(df[columna], kde=True)
    plt.title(f"Distribución de {columna}")
    plt.show()

🔹 5️⃣ Programa Principal (main.py)

from data_loader import cargar_datos_csv, cargar_datos_sheets
from mysql_connector import ejecutar_consulta
from analysis import explorar_datos
from visualization import graficar_histograma

# 1️⃣ Cargar datos desde CSV o Google Sheets
df = cargar_datos_csv("data/datos.csv")
# df = cargar_datos_sheets("https://docs.google.com/spreadsheets/d/ID_SHEET")

if df is not None:
    explorar_datos(df)
    graficar_histograma(df, "Edad")  # Cambia "Edad" por la columna que quieras analizar

# 2️⃣ Consulta de datos en MySQL
query = "SELECT * FROM empleados LIMIT 10;"
resultado = ejecutar_consulta(query)
print(resultado)

📌 Para ejecutar el programa:

python main.py

📌 5. Trabajo Colaborativo en GitHub
🚀 Uso básico de Git

git init  # Iniciar repositorio
git add .  # Agregar archivos
git commit -m "Versión inicial"
git branch -M main
git remote add origin URL_DEL_REPO
git push -u origin main

📌 Cuando alguien haga cambios:

git pull origin main

🎯 Resumen

✔️ Carga de datos desde CSV y Google Sheets
✔️ Exploración y limpieza de datos
✔️ Conexión a MySQL y consultas básicas
✔️ Visualización de datos con Matplotlib y Seaborn
✔️ Trabajo colaborativo con GitHub

..................................................................................

🚀 📌 Próximos Pasos
🔹 1️⃣ Completar la Estructura del Proyecto

Asegúrense de que su estructura de carpetas en el proyecto siga este formato:

📂 analisis-datos-python/
   ├── 📜 README.md             # Documentación del proyecto
   ├── 📜 requirements.txt       # Lista de librerías necesarias
   ├── 📂 data/                  # Archivos CSV o Google Sheets
   │     ├── datos.csv           # Archivo de ejemplo
   ├── 📂 config/                # Configuración
   │     ├── credenciales.json   # Credenciales de Google Sheets
   ├── 📂 src/                   # Código fuente del programa
   │     ├── 📜 main.py          # Ejecuta la aplicación principal
   │     ├── 📜 data_loader.py   # Carga de datos desde CSV o Google Sheets
   │     ├── 📜 mysql_connector.py # Conexión a MySQL
   │     ├── 📜 analysis.py      # Exploración y limpieza de datos
   │     ├── 📜 visualization.py # Gráficos y reportes

Ejecuten este comando para crearlo:

mkdir -p analisis-datos-python/{data,config,src}
touch analisis-datos-python/{README.md,requirements.txt}
touch analisis-datos-python/src/{main.py,data_loader.py,mysql_connector.py,analysis.py,visualization.py}

Después, muevan su código actual a las carpetas correspondientes.
🔹 2️⃣ Subir el Proyecto a GitHub

Si no lo han hecho, inicialicen el repositorio y súbanlo:

cd analisis-datos-python
git init
git add .
git commit -m "Versión inicial del proyecto"
git branch -M main
git remote add origin URL_DEL_REPO
git push -u origin main

📌 Para colaborar en equipo:

    Cada persona debe clonar el repositorio con:

git clone URL_DEL_REPO

Para obtener actualizaciones:

git pull origin main

Para subir cambios:

    git add .
    git commit -m "Descripción de los cambios"
    git push origin main

🔹 3️⃣ Configurar requirements.txt

Para asegurarse de que todos tengan las mismas librerías, generen automáticamente requirements.txt con:

pip freeze > requirements.txt

Y para instalar las dependencias en otro entorno:

pip install -r requirements.txt

🔹 4️⃣ Implementar las Conexiones Faltantes

Ahora que ya tienen data_loader.py funcionando, completen las otras partes del proyecto:
🔹 📂 src/mysql_connector.py → Conexión a MySQL

    Asegúrense de que mysql-connector-python está instalado:

    pip install mysql-connector-python

    Agreguen este código para conectar a MySQL y ejecutar consultas:

import mysql.connector

def conectar_mysql():
    """Conecta a una base de datos MySQL y devuelve la conexión."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="tu_base_de_datos"
        )
        print("✅ Conectado a MySQL.")
        return conn
    except Exception as e:
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

📌 Prueben con esta consulta simple en main.py:

from mysql_connector import ejecutar_consulta

query = "SELECT * FROM empleados LIMIT 5;"
resultado = ejecutar_consulta(query)
print(resultado)

🔹 5️⃣ Implementar src/visualization.py

Para visualizar los datos con matplotlib y seaborn, agreguen esto en visualization.py:

import matplotlib.pyplot as plt
import seaborn as sns

def graficar_histograma(df, columna):
    """Genera un histograma de una columna numérica."""
    plt.figure(figsize=(6, 4))
    sns.histplot(df[columna], kde=True)
    plt.title(f"Distribución de {columna}")
    plt.show()

📌 Prueben en main.py:

from visualization import graficar_histograma
from data_loader import cargar_datos_csv

df = cargar_datos_csv("data/datos.csv")

if df is not None:
    graficar_histograma(df, "Edad")  # Reemplazar con una columna numérica válida

🔹 6️⃣ Configurar la API de Google Sheets (src/data_loader.py)

Para trabajar con Google Sheets, deben habilitar la API de Google Sheets y descargar credenciales.json.

    Si aún no lo hicieron, sigan estos pasos:
        Ir a Google Cloud Console
        Crear un nuevo proyecto
        Habilitar la API de Google Sheets
        Crear credenciales (OAuth 2.0 o clave de servicio)
        Descargar el archivo JSON con las credenciales y guardarlo en config/credenciales.json

📌 Luego, agreguen este código a data_loader.py:

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def cargar_datos_sheets(sheet_url):
    """Carga datos desde Google Sheets en un DataFrame."""
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("config/credenciales.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_url(sheet_url).sheet1
        data = sheet.get_all_records()
        df = pd.DataFrame(data)
        print("✅ Datos cargados correctamente desde Google Sheets.\n")
        return df
    except Exception as e:
        print(f"❌ Error al cargar datos desde Google Sheets: {e}")
        return None

📌 Para probarlo:

df = cargar_datos_sheets("https://docs.google.com/spreadsheets/d/ID_DE_TU_SHEET")
print(df.head())

🎯 📌 Resumen

✅ El proyecto ya tiene la estructura básica y carga datos desde CSV.
✅ Faltan integrar MySQL, visualización y Google Sheets API.
✅ Subir el proyecto a GitHub para trabajo colaborativo.
✅ Configurar requirements.txt para instalar dependencias fácilmente.
✅ Documentar el proceso en README.md para facilitar su uso.

