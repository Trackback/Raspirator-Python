__author__ = 'trackback'
from SocketServer import SocketServer
from Loger import Loger
from CommandsCenter import CommandsCenter
import subprocess

tag = "CommandsCenter"
sock = SocketServer.SocketServer()
debug = Loger.Loger()
commands = CommandsCenter.CommandsCenter()

class Core:
    def __init__(self):
        pass

    def callback(self, data):
        debug.i(tag, "'"+data+"'")
        args = commands.parse([data])
        print(args)
        if args.info:
            sock.say("You request info")

        elif args.quit:
            debug.i(tag, "Server shutdown...")
            sock.shutdown()
        elif args.launch:
            command = args.launch.strip()
            debug.w(tag, command)
            p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            sock.say(output.decode("UTF-8"))
        elif args.echo:
            text = args.echo.strip()
            debug.w(tag, text)
            sock.say("You say: "+text)
        else:
            sock.say("Command "+data+" not found")

    def boot(self):
        sock.start("localhost", 9091, self.callback)
        sock.loop()

