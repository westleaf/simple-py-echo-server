class SocketRegistry:
  def __init__(self):
    self.__sockets = []

  def register(self, socket):
    self.__sockets.append(socket)

  def unregister(self, socket):
    self.__sockets.remove(socket)

  def list_active_sockets(self):
    return [s.getpeername() for s in self.__sockets]
