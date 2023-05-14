import requests
import tkinter as tk
from tkinter import ttk
from datetime import datetime


def obtener_clima(ciudad, clave_api):
    url = f"http://api.weatherapi.com/v1/current.json?key={clave_api}&q={ciudad}"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if "error" not in datos:
        clima_actual = datos["current"]["condition"]["text"]
        temperatura = datos["current"]["temp_c"]
        humedad = datos["current"]["humidity"]
        viento = datos["current"]["wind_kph"]

        resultado_label.config(text=f"Clima en {ciudad}: {clima_actual}\n"
                                    f"Temperatura: {temperatura}°C\n"
                                    f"Humedad: {humedad}%\n"
                                    f"Velocidad del viento: {viento} km/h")
    else:
        resultado_label.config(text="No se pudo obtener el clima para esa ubicación.")


def obtener_clima_ciudad():
    ciudad = ciudad_entry.get()
    clave_api = "ef6c53b9e6214a8399e210711231405"  # Reemplaza esto con tu clave de la API de WeatherAPI.com

    obtener_clima(ciudad, clave_api)


# Función para actualizar la hora actual
def actualizar_hora():
    hora_actual = datetime.now().strftime("%H:%M:%S")
    hora_label.config(text=f"Hora actual: {hora_actual}")
    # Actualizar cada segundo (1000 ms)
    hora_label.after(1000, actualizar_hora)


# Crear ventana
window = tk.Tk()
window.title('Obtener Clima')

# Estilos
window.configure(bg='#ECECEC')
window.geometry('300x250')

# Estilo para el botón
style = ttk.Style()
style.configure('TButton',
                background='#4CAF50',
                foreground='white',
                font=('Arial', 12, 'bold'),
                padding=10)

# Estilo para las etiquetas
style.configure('TLabel',
                background='#ECECEC',
                foreground='#333333',
                font=('Arial', 10))

# Etiqueta
ciudad_label = ttk.Label(window, text='Ciudad:')
ciudad_label.pack()

# Entrada de texto
ciudad_entry = ttk.Entry(window)
ciudad_entry.pack()

# Botón obtener clima
obtener_clima_button = ttk.Button(window, text='Obtener Clima', command=obtener_clima_ciudad)
obtener_clima_button.pack(pady=10)

# Etiqueta de resultado
resultado_label = ttk.Label(window, text='')
resultado_label.pack()

# Etiqueta de hora actual
hora_label = ttk.Label(window, text='')
hora_label.pack()

# Actualizar hora
actualizar_hora()

# Ejecutar ventana
window.mainloop()
