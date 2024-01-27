import socket

HOST = 'localhost'  
PORT = 8000       


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))
print('Connected to', (HOST, PORT))

message = str(input("enter a message:"))
client_socket.sendall(message.encode())
print('Sent message', message)

data = client_socket.recv(1024)
reversed_message = data.decode()
print('Received reversed message', reversed_message)

client_socket.close()
print('Connection closed')
