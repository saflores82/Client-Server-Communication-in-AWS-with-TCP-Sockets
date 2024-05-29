# Client-Server-Communication-in-AWS-with-TCP-Sockets

# Práctica de Comunicación Cliente-Servidor en AWS con Sockets TCP

Este proyecto demuestra cómo configurar y utilizar instancias EC2 en AWS para implementar una comunicación cliente-servidor utilizando sockets TCP en Python.

## Objetivo

- Configurar una instancia EC2 en AWS.
- Implementar un servidor o un cliente en Python para establecer comunicación utilizando sockets TCP.
- Experimentar con la comunicación entre instancias EC2 en la nube.

## Instrucciones

### 1. Configuración de la Instancia EC2

1. Inicia sesión en tu cuenta de AWS.
2. Navega hasta el servicio EC2.
3. Haz clic en "Launch Instance" para iniciar el proceso de creación de una nueva instancia EC2.
4. Selecciona una AMI (Amazon Machine Image). Por ejemplo, puedes elegir una AMI de Ubuntu.
5. Elige el tipo de instancia deseado, configura la red, el almacenamiento y otras opciones según tus preferencias.
6. En la sección de "Security Group", asegúrate de configurar un grupo de seguridad que permita el tráfico TCP en el puerto 8080.
7. Revisa y confirma tu configuración, luego haz clic en "Launch" para iniciar la instancia EC2.

### 2. Elección de Roles

1. Cada alumno debe elegir si desea ser el servidor o el cliente.
2. Una vez que hayan elegido, deben buscar un compañero de trabajo que haya elegido el rol opuesto.

### 3. Implementación del Servidor o Cliente

#### Si decides ser el servidor:

1. Conéctate a tu instancia EC2 utilizando SSH.
2. Crea un nuevo archivo Python llamado `server.py`.
3. Abre `server.py` con tu editor de texto y copia el siguiente código:

    ```python
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
    ```

#### Si decides ser el cliente:

1. Conéctate a tu instancia EC2 utilizando SSH.
2. Crea un nuevo archivo Python llamado `client.py`.
3. Abre `client.py` con tu editor de texto y copia el siguiente código:

    ```python
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
    ```

    **Nota:** Reemplaza `XXXXXXXX` con la dirección IP pública de la instancia EC2 que actúa como servidor.

### 4. Ejecución y Prueba

#### Para el servidor:

1. En la instancia EC2 que actuará como servidor, ejecuta el siguiente comando para iniciar el servidor:
    ```bash
    python3 server.py
    ```

#### Para el cliente:

1. En la instancia EC2 que actuará como cliente, ejecuta el siguiente comando para iniciar el cliente:
    ```bash
    python3 client.py
    ```

2. Sigue las instrucciones en pantalla para enviar mensajes entre el cliente y el servidor. El cliente enviará un mensaje al servidor y recibirá una respuesta.

## Conclusión

Esta práctica proporciona una comprensión básica de cómo configurar y utilizar instancias EC2 en AWS para implementar una comunicación cliente-servidor utilizando sockets TCP en Python. Siguiendo estos pasos, puedes experimentar con la comunicación entre instancias en la nube y entender mejor cómo funciona la red y la programación de sockets.

