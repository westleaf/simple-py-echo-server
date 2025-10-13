class SocketRegistry:
  def __init__(self):
    self.__sockets = []

  def register(self, socket):
    self.__sockets.append(socket)

  def unregister(self, socket):
    self.__sockets.remove(socket)

  def list_active_sockets(self):
    return [s.getpeername() for s in self.__sockets]

  def broadcast(self, message: bytes, exclude_socket=None):
    for socket in self.__sockets:
      if socket is not exclude_socket:
        try:
          socket.sendall(message)
        except OSError:
          pass
