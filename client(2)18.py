import socket as sk

client = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

client.sendto("binary.bin".encode(), ('localhost', 5500))

data, address = client.recvfrom(1024)

file = open("rfile2.bin", "wb")
file.write(data)
client.close()
