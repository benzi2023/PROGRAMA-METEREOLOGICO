import requests

def obtener_clima(ciudad, clave_api):
    url = f"http://api.weatherapi.com/v1/current.json?key={clave_api}&q={ciudad}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    if "error" not in datos:
        clima_actual = datos["current"]["condition"]["text"]
        temperatura = datos["current"]["temp_c"]
        humedad = datos["current"]["humidity"]
        viento = datos["current"]["wind_kph"]
        
        print(f"Clima en {ciudad}: {clima_actual}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Humedad: {humedad}%")
        print(f"Velocidad del viento: {viento} km/h")
    else:
        print("No se pudo obtener el clima para esa ubicación.")

ciudad = input("Ingrese el nombre de la ciudad: ")
clave_api = "ef6c53b9e6214a8399e210711231405"  # Reemplaza esto con tu clave de la API de WeatherAPI.com

obtener_clima(ciudad, clave_api)
