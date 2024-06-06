import socket
import threading
import rsa

public_key, private_key = rsa.newkeys(1024)

public_partner = None

choice = input("Do you want to host the server (1) or to connect to a server (2): ")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.0.138", 9999))
    server.listen()

    client, _ = server.accept()
    # Send the public key to the client in format PEM
    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.0.138", 9999))
    # Receive the public key from the server in format PEM
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    # Send the public key to the server in format PEM
    client.send(public_key.save_pkcs1("PEM"))
else:
    exit()

def send(c):
    while True:
        message = input()
        c.send(rsa.encrypt(message.encode(), public_partner))
        print("You: " + message)

def receive(c):
    while True:
        message = rsa.decrypt(c.recv(1024), private_key).decode()
        print("User: " + message)

threading.Thread(target=send, args=(client,)).start()
threading.Thread(target=receive, args=(client,)).start()
