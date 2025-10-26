class SocketRegistry:
  def __init__(self):
    self.__sockets = []

  def register(self, socket):
    self.__sockets.append(socket)

  def unregister(self, socket):
    try:
      self.__sockets.remove(socket)
    except ValueError:
      pass  # Socket not in list

  def list_active_sockets(self):
    return self.__sockets.copy()

  def broadcast(self, message: bytes, exclude_socket=None):
    # Create a copy to avoid modification during iteration
    sockets_copy = self.__sockets.copy()
    for socket in sockets_copy:
      if socket is not exclude_socket:
        try:
          socket.sendall(message)
        except OSError:
          # Remove dead sockets automatically
          try:
            self.unregister(socket)
          except ValueError:
            pass  # Socket already removed
