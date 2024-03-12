import pandas as pd
import json

# Lee el archivo Excel
excel_file = 'type.xlsx'  # Reemplaza 'archivo_excel.xlsx' con el nombre de tu archivo Excel
data_frame = pd.read_excel(excel_file)

# Crea un diccionario para almacenar los datos
data_dict = {}

# Itera sobre las filas del DataFrame y guarda los valores en el diccionario
for index, row in data_frame.iterrows():
    key = str(row['A'])  # Columna A como clave
    value = str(row['B'])  # Columna B como valor, convertida a str
    data_dict[key] = value

# Genera el archivo JSON
json_file = 'datos.json'  # Nombre del archivo JSON de salida
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=4)

print("Se ha creado el archivo JSON correctamente.")
