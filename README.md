# 2c.SIMULATING ARP /RARP PROTOCOLS
## REGNO: 212225040117
## NAME: HARISH PRANAV
## AIM
To write a python program for simulating ARP protocols using TCP.
## ALGORITHM:
## Client:
1. Start the program
2. Using socket connection is established between client and server.
3. Get the IP address to be converted into MAC address.
4. Send this IP address to server.
5. Server returns the MAC address to client.
## Server:
1. Start the program
2. Accept the socket which is created by the client.
3. Server maintains the table in which IP and corresponding MAC addresses are
stored.
4. Read the IP address which is send by the client.
5. Map the IP address with its MAC address and return the MAC address to client.
P
## PROGRAM - ARP
## `SERVER`
```python
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
```
## `CLIENT`
```python
import socket

HOST = "127.0.0.1"
PORT = 9001

ip_address = input("Enter an IP address: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(ip_address.encode())
    mac_address = client.recv(1024).decode()

print("MAC address:", mac_address)
```
## OUPUT - ARP
<img width="1117" height="272" alt="image" src="https://github.com/user-attachments/assets/30f214b0-03b6-402b-97c6-4e9d96c137b0" />

## PROGRAM - RARP
## `SERVER`
```python
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
```
## `CLIENT`
```python
import socket

HOST = "127.0.0.1"
PORT = 9002

mac_address = input("Enter a MAC address: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(mac_address.encode())
    ip_address = client.recv(1024).decode()

print("IP address:", ip_address)
```
## OUPUT -RARP
<img width="1103" height="166" alt="image" src="https://github.com/user-attachments/assets/e79fa4db-a592-402a-a4c5-775d2fb6f37e" />

## RESULT
Thus, the python program for simulating ARP protocols using TCP was successfully 
executed.
