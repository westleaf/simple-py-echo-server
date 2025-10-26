import socket
import threading
import time
import datetime

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
            thread.daemon = True  # Daemon threads will close when main thread exits
            thread.start()
            print(f"Active connections: {threading.active_count() - 1}")

def handle_client(conn: socket, addr):
    print(f"Connection established with {addr} ")
    registry.register(conn)
    try:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received from {addr}: {data.decode()}")
                timestamp = str(datetime.datetime.now()).split('.')[0]
                message = f"{timestamp} - {data.decode()}".encode()
                conn.sendall(message)
                registry.broadcast(message, exclude_socket=conn)
            except ConnectionResetError:
                print(f"Client {addr} disconnected")
                break
            except Exception as e:
                print(f"Error handling client {addr}: {e}")
                break
    finally:
        # Clean up when client disconnects
        registry.unregister(conn)
        conn.close()
        print(f"Connection with {addr} closed. Active connections: {threading.active_count() - 1}")

def stop_server():
    print("\nServer is stopping...")
    for connection in registry.list_active_sockets():
        try:
            connection.close()
        except:
            pass
    print("All connections closed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_server()
