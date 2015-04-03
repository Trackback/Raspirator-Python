__author__ = 'trackback'

from Loger import Loger
from Core import Core

core = Core()

tag = "Boot"
debug = Loger()

debug.i(tag, "Initing")
core.boot()
debug.i(tag, "Finish")