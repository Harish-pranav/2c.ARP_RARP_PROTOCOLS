import socket

HOST = "127.0.0.1"
PORT = 9002

mac_address = input("Enter a MAC address: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(mac_address.encode())
    ip_address = client.recv(1024).decode()

print("IP address:", ip_address)