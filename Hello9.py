import socket

HOST = 'localhost'  
PORT = 8000         


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = str(input("enter a message"))
client_socket.sendto(message.encode(), (HOST, PORT))
print('Sent message', message)

data, server_address = client_socket.recvfrom(1024)
received_message = data.decode()
print('Received message', received_message, 'from', server_address)

client_socket.close()
print('Socket closed')
