GUIA PARA PROYECTO

---

## **1️⃣ Descripción del Proyecto**
### 🎯 **Objetivo General**
El objetivo de este proyecto es desarrollar un programa en **Python** que permita la manipulación y análisis de datos mediante diversas tecnologías, incluyendo **Google Sheets API, MySQL y visualización de datos**. 

✅ **Objetivos específicos**:
- Cargar y limpiar datos desde **Google Sheets** y archivos CSV.
- Explorar y visualizar datos utilizando **Pandas y Matplotlib**.
- Conectar a una base de datos **MySQL** y ejecutar consultas SQL.
- Generar reportes estructurados en **Google Looker Studio**.
- Gestionar el código de forma colaborativa usando **GitHub**.

✔️ **Tecnologías y herramientas utilizadas**:
- **Manipulación de datos**: Pandas, NumPy
- **Visualización de datos**: Matplotlib, Seaborn
- **Conexión con Google Sheets**: Google Sheets API (gspread, oauth2client)
- **Base de datos**: MySQL (mysql-connector-python)
- **Automatización y autenticación**: Python, Google Cloud Credentials
- **Trabajo colaborativo**: GitHub

---

## **2️⃣ Instalación de Librerías Necesarias**
Antes de comenzar, asegúrate de instalar todas las librerías necesarias ejecutando:

```bash
pip install pandas numpy matplotlib seaborn mysql-connector-python gspread oauth2client google-auth google-auth-oauthlib google-auth-httplib2
```

📌 **Explicación de las librerías:**
- **Pandas y NumPy** → Para manipulación de datos.
- **Matplotlib y Seaborn** → Para visualización de datos.
- **MySQL Connector** → Para conectarse a bases de datos MySQL.
- **gspread y oauth2client** → Para integración con **Google Sheets API**.
- **google-auth** → Para autenticación con Google Cloud API.

---

## **3️⃣ Organización del Proyecto** (Estructura actualizada)

📂 `analisis-datos-python/`
   ├── 📜 `README.md` *(Documentación del proyecto)*
   ├── 📜 `requirements.txt` *(Lista de librerías necesarias)*
   ├── 📂 `config/` *(Archivos de configuración y credenciales)*
   │     ├── 📜 `credenciales.json` *(Credenciales de Google Sheets API)*
   │     ├── 📜 `auth_script.py` *(Script para autenticación con Google)*
   ├── 📂 `data/` *(Archivos CSV o datos extraídos)*
   ├── 📂 `src/` *(Código fuente del proyecto)*
   │     ├── 📜 `main.py` *(Ejecuta la aplicación principal)*
   │     ├── 📜 `data_loader.py` *(Carga de datos desde Google Sheets o CSV)*
   │     ├── 📜 `mysql_connector.py` *(Conexión y consultas a MySQL)*
   │     ├── 📜 `analysis.py` *(Exploración y limpieza de datos)*
   │     ├── 📜 `visualization.py` *(Visualización y reportes de datos)*
   ├── 📂 `venv/` *(Entorno virtual de Python)*
   ├── 📂 `PROBLEMAS_SURGIDOS.txt` *(Registro de errores y soluciones encontradas)*

---

## **4️⃣ Desarrollo Paso a Paso**

### **🔹 1️⃣ Autenticación con Google Sheets API (`auth_script.py`)**
Antes de cargar datos desde Google Sheets, es necesario autenticarse con la **API de Google Sheets** utilizando credenciales de cuenta de servicio.

📜 **Código en `config/auth_script.py`**:

```python
from google.oauth2 import service_account

# Ruta al archivo de credenciales
credenciales_path = "/home/reboot-student/code/labs/PROYECTS/analisis-datos-python/config/credenciales.json"

# Cargar credenciales
credentials = service_account.Credentials.from_service_account_file(credenciales_path)

# Verificar si se cargó correctamente
print("✅ Autenticación exitosa")
```

📌 **Ejecución**:
```bash
python config/auth_script.py
```

---

### **🔹 2️⃣ Carga de Datos desde CSV o Google Sheets (`data_loader.py`)**
📜 **Código en `src/data_loader.py`**:

```python
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Ruta al archivo de credenciales
credenciales_path = "/home/reboot-student/code/labs/PROYECTS/analisis-datos-python/config/credenciales.json"

# Cargar credenciales
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file(credenciales_path, scopes=scope)
client = gspread.authorize(creds)

def cargar_datos_sheets(sheet_url):
    """Carga datos desde Google Sheets en un DataFrame."""
    try:
        sheet = client.open_by_url(sheet_url).sheet1
        data = sheet.get_all_records()
        df = pd.DataFrame(data)
        print("✅ Datos cargados correctamente desde Google Sheets.\n")
        return df
    except Exception as e:
        print(f"❌ Error al cargar datos desde Google Sheets: {e}")
        return None
```

📌 **Para probarlo**:
```python
df = cargar_datos_sheets("https://docs.google.com/spreadsheets/d/ID_SHEET")
print(df.head())
```

---

### **🔹 3️⃣ Conexión a MySQL y Ejecución de Consultas (`mysql_connector.py`)**
📜 **Código en `src/mysql_connector.py`**:

```python
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
    conn = conectar_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        conn.close()
        return resultado
```

📌 **Para ejecutar una consulta**:
```python
query = "SELECT * FROM empleados LIMIT 10;"
resultado = ejecutar_consulta(query)
print(resultado)
```

---

### **🔹 4️⃣ Exploración y Limpieza de Datos (`analysis.py`)**
📜 **Código en `src/analysis.py`**:

```python
def explorar_datos(df):
    """Muestra información y estadísticas básicas."""
    print(df.info())
    print("\nEstadísticas:")
    print(df.describe())
```

📌 **Ejemplo de uso**:
```python
df = cargar_datos_sheets("https://docs.google.com/spreadsheets/d/ID_SHEET")
explorar_datos(df)
```

---

### **🔹 5️⃣ Visualización de Datos (`visualization.py`)**
📜 **Código en `src/visualization.py`**:

```python
import matplotlib.pyplot as plt
import seaborn as sns

def graficar_histograma(df, columna):
    """Genera un histograma de una columna numérica."""
    plt.figure(figsize=(6, 4))
    sns.histplot(df[columna], kde=True)
    plt.title(f"Distribución de {columna}")
    plt.show()
```

📌 **Ejemplo de uso**:
```python
graficar_histograma(df, "Edad")
```

---

### **🔹 6️⃣ Programa Principal (`main.py`)**
📜 **Código en `src/main.py`**:

```python
from data_loader import cargar_datos_sheets
from mysql_connector import ejecutar_consulta
from analysis import explorar_datos
from visualization import graficar_histograma

# Cargar datos desde Google Sheets
df = cargar_datos_sheets("https://docs.google.com/spreadsheets/d/ID_SHEET")

if df is not None:
    explorar_datos(df)
    graficar_histograma(df, "Edad")  # Cambia "Edad" por la columna deseada
```

📌 **Ejecutar**:
```bash
python src/main.py
```

---

## **📌 Resumen**
✔️ Integración con Google Sheets  
✔️ Conexión con MySQL  
✔️ Carga y exploración de datos  
✔️ Visualización y reportes  
✔️ Trabajo colaborativo en GitHub 🚀


