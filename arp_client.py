import socket

HOST = "127.0.0.1"
PORT = 9001

ip_address = input("Enter an IP address: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(ip_address.encode())
    mac_address = client.recv(1024).decode()

print("MAC address:", mac_address)