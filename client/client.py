import socket

HOST = "127.0.0.1"
PORT = 65432

def main():
  name = input("Enter your name ").strip(" ")
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, PORT))
      while True:
        message = name + ": " + input("Enter message to send to server: ")
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"{data.decode()}")
  except Exception as e:
    print(f"could not connect ${e}")

if __name__ == "__main__":
    try:
      main()
    except KeyboardInterrupt:
      print("Client is stopping...")
    except ConnectionResetError:
      print("Connection was reset...")
