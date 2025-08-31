import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 12345))

    print("UDP Server is ready to receive data...")
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
        server_socket.sendto("Message received!".encode(), addr)

if __name__ == "__main__":
    udp_server()
