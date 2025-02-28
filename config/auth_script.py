from google.oauth2 import service_account

# Ruta al archivo de credenciales
credenciales_path = "/home/reboot-student/code/labs/PROYECTS/analisis-datos-python/config/credenciales.json"

# Cargar credenciales
credentials = service_account.Credentials.from_service_account_file(credenciales_path)

# Verificar si se cargó correctamente
print("✅ Autenticación exitosa")





