import socket

HOST = "127.0.0.1"
PORT = 9001

ip_to_mac = {
    "192.168.1.10": "AA:BB:CC:DD:EE:01",
    "192.168.1.20": "AA:BB:CC:DD:EE:02",
    "192.168.1.30": "AA:BB:CC:DD:EE:03",
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("ARP server waiting for a client...")

    connection, address = server.accept()
    with connection:
        print("Connected by:", address)
        ip_address = connection.recv(1024).decode().strip()
        mac_address = ip_to_mac.get(ip_address, "IP address not found")
        connection.sendall(mac_address.encode())