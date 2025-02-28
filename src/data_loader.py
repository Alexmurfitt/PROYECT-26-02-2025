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
