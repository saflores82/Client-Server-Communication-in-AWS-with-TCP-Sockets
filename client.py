import socket
 
# Dirección IP y puerto del servidor
HOST = 'XXXXXXXX'
PORT = 8080
 
# Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conectar el socket al servidor
    s.connect((HOST, PORT))
    while True:
        # Enviar un mensaje al servidor
        message = input('Escribe tu mensaje al servidor: ')
        s.sendall(message.encode())
        # Recibir respuesta del servidor
        data = s.recv(1024)
        print('Respuesta del servidor:', data.decode()) 

