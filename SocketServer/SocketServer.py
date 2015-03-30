__author__ = 'trackback'
import asyncore, socket
from Loger import Loger

debug = Loger.Loger()
tag = "Socket"


class SocketServer(asyncore.dispatcher):
    def __init__(self):
        pass

    def start(self, port, callback):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('', port))
        self.listen(1)
        self.callback = callback

    def handle_accept(self):
        # when we get a client connection start a dispatcher for that
        # client
        socket, address = self.accept()
        debug.i(tag, 'Connection by '+address[0])
        EchoHandler(socket)

    def loop(self):
        asyncore.loop()


class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        self.out_buffer = self.recv(1024)
        if not self.out_buffer:
            self.close()
        data = self.out_buffer.decode("UTF-8")
        debug.i(tag, data)
        #self.callback(data)