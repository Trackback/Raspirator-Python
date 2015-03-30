__author__ = 'trackback'
from SocketServer import SocketServer
from Loger import Loger
from CommandsCenter import CommandsCenter

tag = "CommandsCenter"
sock = SocketServer.SocketServer()
debug = Loger.Loger()
commands = CommandsCenter.CommandsCenter()

class Core:
    def __init__(self):
        pass

    def callback(self, data):
        debug.i(tag, data)
        args = commands.parse([data])
        if args.info:
            sock.say("You request info")

        if args.quit:
            debug.i(tag, "Server shutdown...")
            sock.shutdown()

        return None

    def boot(self):
        sock.start(9091, self.callback)
        sock.loop()
