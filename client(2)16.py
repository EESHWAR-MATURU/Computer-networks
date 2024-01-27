import socket

host = 'localhost'
port = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

while True:
    filename = input('Enter filename to request (or q to quit): ')

    if filename.lower() == 'q':
        break

    client_socket.sendall(filename.encode())

    data = client_socket.recv(1024)

    if data:
        with open("16 recv2.txt", 'wb') as file:
            file.write(data)
        print('File received and saved as {}'.format(filename))
    else:
        print('Error: {}'.format(data.decode()))

client_socket.close()
