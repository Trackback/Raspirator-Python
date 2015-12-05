import pyttsx

__author__ = 'trackback'
from SocketServer import SocketServer
from Loger import Loger
from CommandsCenter import CommandsCenter
import subprocess
from pyttsx import *

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
        elif args.say:
            tts = pyttsx.init()
            tts.setProperty("rate", 140)
            tts.setProperty('voice', bytes("russian", "UTF-8"))
            text = args.say.strip()
            tts.say(text)
            tts.runAndWait()
            tts.stop()
        else:
            sock.say("Command "+data+" not found")

    def boot(self):
        sock.start("localhost", 9091, self.callback)
        sock.loop()

