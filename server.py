import socket
 
# Dirección IP y puerto en el que el servidor va a escuchar
HOST = '0.0.0.0'
PORT = 8080
 
# Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Asociar el socket a la dirección y puerto especificados
    s.bind((HOST, PORT))
    # Esperar por conexiones entrantes (máximo 1 cliente en la cola)
    s.listen(1)
    print('Esperando conexiones entrantes...')
    # Aceptar la conexión entrante
    conn, addr = s.accept()
    with conn:
        print('Conexión entrante desde:', addr)
        while True:
            # Recibir datos del cliente
            data = conn.recv(1024)
            if not data:
                break
            print('Mensaje recibido del cliente:', data.decode())
            # Enviar respuesta al cliente
            response = input('Escribe tu mensaje al cliente: ')
            conn.sendall(response.encode())
