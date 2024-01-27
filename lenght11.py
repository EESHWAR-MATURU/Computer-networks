import socket

HOST = 'localhost' 
PORT = 8000         
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = str(input("Enter a message:"))
client_socket.sendto(message.encode(), (HOST, PORT))
print('Sent message', message)

length, server_address = client_socket.recvfrom(1024)
print('Received length', length.decode().strip(), 'from', server_address)

client_socket.close()
print('Socket closed')
