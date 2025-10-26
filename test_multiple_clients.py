#!/usr/bin/env python3
"""
Test script to simulate multiple clients connecting to the server
"""
import socket
import threading
import time
import sys

HOST = "127.0.0.1"
PORT = 65432

def client_worker(client_id, num_messages=3):
    """Simulate a client that connects, sends messages, and disconnects"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f"Client {client_id} connected")

            for i in range(num_messages):
                message = f"Client{client_id}: Message {i+1}"
                s.sendall(message.encode())

                # Receive response
                response = s.recv(1024)
                print(f"Client {client_id} received: {response.decode()}")

                time.sleep(1)  # Wait between messages

            print(f"Client {client_id} finished")

    except Exception as e:
        print(f"Client {client_id} error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python test_multiple_clients.py <num_clients>")
        sys.exit(1)

    num_clients = int(sys.argv[1])
    print(f"Starting {num_clients} test clients...")

    threads = []
    for i in range(num_clients):
        thread = threading.Thread(target=client_worker, args=(i+1,))
        threads.append(thread)
        thread.start()
        time.sleep(0.5)  # Stagger client connections

    # Wait for all clients to finish
    for thread in threads:
        thread.join()

    print("All test clients finished")

if __name__ == "__main__":
    main()
