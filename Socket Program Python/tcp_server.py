import socket

def responsive_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(10)

    print("Server is listening for connections...")
    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode()
        print(f"Received: {data}")
        conn.send("Message received!".encode())  # Send response back
        conn.close()

if __name__ == "__main__":
    responsive_server()
