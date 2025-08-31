import socket

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))

    client_socket.send("Hello, TCP Server!".encode())
    data = client_socket.recv(1024).decode()  # Receive server response
    print(f"Server Response: {data}")
    client_socket.close()

if __name__ == "__main__":
    tcp_client()
