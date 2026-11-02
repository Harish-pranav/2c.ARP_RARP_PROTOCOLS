import socket

HOST = "127.0.0.1"
PORT = 9002

mac_to_ip = {
    "AA:BB:CC:DD:EE:01": "192.168.1.10",
    "AA:BB:CC:DD:EE:02": "192.168.1.20",
    "AA:BB:CC:DD:EE:03": "192.168.1.30",
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("RARP server waiting for a client...")

    connection, address = server.accept()
    with connection:
        print("Connected by:", address)
        mac_address = connection.recv(1024).decode().strip().upper()
        ip_address = mac_to_ip.get(mac_address, "MAC address not found")
        connection.sendall(ip_address.encode())