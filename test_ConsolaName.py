import ctypes
import time

# Define el título de la consola
console_title = "Mi Consola Personalizada"
console = "Nombre de Consola"

# Cambia el título de la consola
ctypes.windll.kernel32.SetConsoleTitleW(console_title)
time.sleep(3)
ctypes.windll.kernel32.SetConsoleTitleW(console)
time.sleep(3)

# El resto de tu código va aquí
print("Este es el nuevo título de la consola.")
# ...
