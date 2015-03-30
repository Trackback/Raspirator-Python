__author__ = 'trackback'
import socket
from Loger import Loger

debug = Loger.Loger()
tag = "Socket"


class SocketServer:
    def __init__(self, sock=None, conn=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.conn = conn

    def start(self, port, callback):
        self.callback = callback
        self.sock = socket.socket()
        debug.i(tag, "Binding "+socket.gethostname())
        self.sock.bind(("", port))
        debug.i(tag, "Listening...")
        self.sock.listen(5)
        debug.i(tag, "Wait for client...")
        (self.conn, addr) = self.sock.accept()
        debug.i(tag, "Connection success")
        self.catchData()

    def catchData(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                debug.i(tag, 11)
                break
            data = data.decode("utf-8")
            self.callback(data)

    def shutdown(self):
        debug.i(tag, "Shutdown")
        self.conn.close()

    def say(self, data):
        debug.i(tag, "Sending data: "+data)
        self.conn.send(bytes(data, "UTF-8"))
