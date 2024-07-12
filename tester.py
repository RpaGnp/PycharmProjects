# import mysql.connector

# def connect_to_mysql():
#     try:
#         # Establece la conexión
#         connection = mysql.connector.connect(
#             host="10.206.170.19",  # Cambia esto si tu base de datos está en un servidor remoto
#             user="BotCndCali",
#             password="B0tCndC4Li24*",
#             database="dbcrmgnp"
#         )

#         if connection.is_connected():
#             print("Conexión exitosa a MySQL")
            
#             # Crea un cursor para ejecutar consultas
#             cursor = connection.cursor()

#             # Ejemplo de consulta
#             cursor.execute("SELECT * FROM dbcrmcalv2.tbl_hasigbacklog order by asb_nid desc limit 10;")

#             # Obtiene los resultados
#             results = cursor.fetchall()

#             # Imprime los resultados
#             for row in results:
#                 print(row)

#             # Cierra el cursor y la conexión
#             cursor.close()
#             connection.close()
#             print("Conexión cerrada")

#     except mysql.connector.Error as error:
#         print(f"Error al conectarse a MySQL: {error}")

# # Llama a la función
# connect_to_mysql()



import os

paths = [
    "C:/Users/USER/PycharmProjects/Bot_server/bot_server.py",
    "C:/Users/USER/PycharmProjects/Bot_server/img/logo-removebg-preview.ico",
    "C:/Users/USER/PycharmProjects/Bot_server",
    "C:/Users/USER/PycharmProjects/Bot_server/dist",
    "C:/Users/USER/PycharmProjects/Bot_server/build",
]

for path in paths:
    if not os.path.exists(path):
        print(f"Path not found: {path}")
    else:
        print(f"Path exists: {path}")