import requests
import json

base_url = "https://apps.lider.cl/supermercado/bff/products/"

querystring = {"page":"1","sc":"1"}

headers = {
    "cookie": "TSe3289311027=080d3e3cf5ab2000185f84d10f37820d202fba57434e43ec1d69e092719f595879586f5efab65b800845332bd4113000726079d93dc75b25b64b84d0d8daed3b46f92e6d0652f1c80dd082c3faa24b45060ae1aaab08878fc132938e9148c3e0; TS01cc7ea9=0179207e648e98a03ef3632925172925131a1ef1e215028d49f8374128e91affad272d7a486b1baeb7bc8a916dc15f7a3599bd47fd; TS017e8d10=0179207e648e98a03ef3632925172925131a1ef1e215028d49f8374128e91affad272d7a486b1baeb7bc8a916dc15f7a3599bd47fd",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,es-CL;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.santaisabel.cl/",
    "apiKey": "WlVnnB7c1BblmgUPOfg",
    "Content-Type": "application/json",
    "x-consumer": "santaisabel",
    "x-account": "valdiviachacabuco",
    "Origin": "https://www.santaisabel.cl",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Connection": "keep-alive"
}



# Definir el rango de valores para probar
inicio_rango = int(input("Inicio del rango: "))  # Cambia esto al valor inicial de tu rango
fin_rango = int(input("Fin del rango: "))    # Cambia esto al valor final de tu rango

skus = {}  

# Bucle para probar cada valor en el rango
for value in range(inicio_rango, fin_rango + 1):
    url = base_url + str(value)
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        print(f"El SKU {value} funciona.")
        data = response.json()  # Asegúrate de hacer algo con data si es necesario
        skus[value] = data  # Agregar los datos al diccionario skus

with open(f'resultados{inicio_rango}-{fin_rango}.json', 'w') as f:
    json.dump(skus, f)

print(f"Resultados guardados en 'resultados.json'")
