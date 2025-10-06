import socket

HOST = "127.0.0.1"
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = "Hello, Server!"
        s.sendall(message.encode())
        data = s.recv(1024)
    print(f"Received {data.decode()}")

if __name__ == "__main__":
    main()
