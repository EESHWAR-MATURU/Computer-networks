import socket

host = "127.0.0.1"
port = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
    message = input("Enter message: ")

    client_socket.sendall(message.encode("utf-8"))

    if message == "Bye":
        break

    data = client_socket.recv(1024).decode("utf-8")
    print(data)

    if data == "You said: Bye":
        break

client_socket.close()
