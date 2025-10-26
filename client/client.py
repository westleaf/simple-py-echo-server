import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 65432

def main():
    name = input("Enter your name: ").strip()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(f"{name} connected!".encode())
            print(f"Connected to server at {HOST}:{PORT}")
            print("Type 'quit' to exit")

            # Start listening thread
            listener_thread = threading.Thread(target=listen_for_messages, args=(s,))
            listener_thread.daemon = True
            listener_thread.start()

            # Send messages
            while True:
                try:
                    message = input()
                    if message.lower() in ['quit', 'exit']:
                        break

                    full_message = f"{name}: {message}"
                    s.sendall(full_message.encode())

                except KeyboardInterrupt:
                    print("\nDisconnecting...")
                    break
                except Exception as e:
                    print(f"Error sending message: {e}")
                    break

    except Exception as e:
        print(f"Could not connect: {e}")

def listen_for_messages(sock):
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                print("Server closed the connection")
                break

            message = data.decode()
            # Clear current input line and print received message
            print(f"\r{message}")
            print("> ", end="", flush=True)

    except Exception as e:
        print(f"Connection lost: {e}")
        # Force exit the main thread
        import os
        os._exit(0)

if __name__ == "__main__":
    try:
      main()
    except KeyboardInterrupt:
      print("Client is stopping...")
    except ConnectionResetError:
      print("Connection was reset...")
