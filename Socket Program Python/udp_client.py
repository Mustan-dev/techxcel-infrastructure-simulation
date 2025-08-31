import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 12345)

    client_socket.sendto("Hello, UDP Server!".encode(), server_address)
    data, _ = client_socket.recvfrom(1024)  # Receive server response
    print(f"Server Response: {data.decode()}")
    client_socket.close()

if __name__ == "__main__":
    udp_client()
