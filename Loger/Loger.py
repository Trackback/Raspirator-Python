__author__ = 'trackback'


class Loger:
    def log(self, tag, data):
        print(tag+">>>", data)

    def w(self, tag, data):
        self.log('[WARNING] '+tag, data)

    def i(self, tag, data):
        self.log('[INFO] '+tag, data)

    def e(self, tag, data):
        self.log('[ERROR] '+tag, data)