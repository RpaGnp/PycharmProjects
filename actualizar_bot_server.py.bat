
            @Echo OFF

            TimeOut /T 5

            taskkill -im bot_server.py -f

            TimeOut /T 3

            DEL /F /Q bot_server.py

            REN C:\Users\USER\PycharmProjects\Bot_server\act_bot_server.py bot_server.py

            START bot_server.py
            
            DEL /F /Q C:\Users\USER\PycharmProjects\Bot_server\act_bot_server.py.bat
            
            DEL /F /Q C:\Users\USER\PycharmProjects\Bot_server\lanzador_bot_server.py.bat

            



            Exit

        