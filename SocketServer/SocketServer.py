__author__ = 'trackback'

import asynchat
import asyncore
import socket
import threading
from Loger import Loger

debug = Loger.Loger()
tag = "Socket"
chat_room = {}


class SocketServer(asyncore.dispatcher):
    def __init__(self):
        pass

    def start(self, host, port, callback):
        asyncore.dispatcher.__init__(self, map=chat_room)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(5)
        self.callback = callback
        debug.i(tag, "Ready!")

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            debug.i(tag, 'Incoming connection from %s' % repr(addr))
            self.sock = sock
            self.handler = ChatHandler(sock, self.callback)

    def loop(self):
        asyncore.loop(map=chat_room)

    def say(self, data):
        self.handler.handle_write(data)

    def shutdown(self):
        self.sock.close()


class ChatHandler(asynchat.async_chat):
    def __init__(self, sock, callback):
        asynchat.async_chat.__init__(self, sock=sock, map=chat_room)
        self.set_terminator('\n')
        self.buffer = []
        self.callback = callback
        self.handle_write("Connection success")

    def collect_incoming_data(self, data):
        self.buffer.append(data)

    def found_terminator(self):
        msg = self.buffer
        debug.i(tag, "Recived: "+msg)
        for handler in chat_room.itervalues():
            if hasattr(handler, 'push'):
                data = bytes(msg, "UTF-8")
                handler.push(data)
        self.buffer = []

    def handle_read(self):
        data = self.recv(1024)
        if data is None:
            return
        data = data.decode("UTF-8")
        debug.i(tag, "read "+data)
        self.callback(data)

    def handle_write(self, data):
        data = bytes(data, "UTF-8")
        self.push(data)
        self.initiate_send()