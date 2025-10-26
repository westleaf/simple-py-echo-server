# Simple Python Echo Server

A multi-threaded TCP server that handles multiple client connections with broadcasting capabilities.

## Features

- **Multi-client support**: Handles multiple simultaneous client connections
- **Message broadcasting**: Messages from one client are broadcast to all other connected clients
- **Proper connection cleanup**: Automatically removes disconnected clients from the registry
- **Thread-safe operations**: Uses threading for concurrent client handling

## Running the Server

```bash
cd server
python server.py
```

The server will start on `127.0.0.1:65432` by default.

## Running a Client

```bash
cd client
python client.py
```

Enter your name when prompted, then start chatting. Type 'quit' or 'exit' to disconnect.

## Testing Multiple Connections

Use the provided test script to simulate multiple clients:

```bash
python test_multiple_clients.py 5
```

This will create 5 test clients that connect, send messages, and disconnect.

## Architecture

### Server Components

- **server.py**: Main server logic with threading support
- **socket_registry.py**: Manages active client connections and broadcasting

### Key Improvements Made

1. **Proper socket cleanup**: Sockets are now properly removed from registry when clients disconnect
2. **Exception handling**: Better error handling for connection issues
3. **Thread management**: Daemon threads for automatic cleanup
4. **Broadcasting fixes**: Fixed parameter naming and dead socket removal
5. **Client improvements**: Simplified threading model with proper cleanup

## Usage Examples

### Start server:
```bash
python server/server.py
```

### Connect multiple clients in separate terminals:
```bash
python client/client.py
```

Messages sent by one client will be echoed back by the server and broadcast to all other connected clients.
