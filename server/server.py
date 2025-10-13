import socket
import threading

from socket_registry import SocketRegistry

HOST = "127.0.0.1"
PORT = 65432
registry = SocketRegistry()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server started on: {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn,addr))
            thread.start()
            print(f"Active connections: {threading.active_count() - 1}")

def handle_client(conn: socket, addr):
    print(f"Connection established with {addr}")
    registry.register(conn)
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Recieved from {addr}: {data.decode()}")
            conn.sendall(f"Server response: {data.decode()}".encode())
            message = f"[{conn.getpeername()}] {data.decode()}".encode()
            registry.broadcast(message)
        except ConnectionResetError:
            print(f"Client {addr} disconnected")
            break

def stop_server():
    print("Server is stopping...")
    for connection in registry.list_active_sockets():
        connection.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_server()
