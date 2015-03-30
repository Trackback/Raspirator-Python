__author__ = 'trackback'

import argparse
from Loger import Loger

debug = Loger.Loger()
tag = "CommandsCenter"


class CommandsCenter:
    def __init__(self, parser=None):
        if parser is None:
            self.parser = argparse.ArgumentParser(description='Raspirator')
        else:
            self.parser = parser
        self.build()

    def build(self):
        self.parser.add_argument('-i', '--info', action="store_true", help="Get info")
        self.parser.add_argument('-q', '--quit', action="store_true", help="Exit")

    def parse(self, data):
        return self.parser.parse_args(data)
