from appcore import app
import logging

class ModuleBase:
    def __init__(self, path):
        self.path = path
        logging.debug(u"ModuleBase inited. Path:{0}".format(path))
        logging.debug(u"Loaded module: {0}".format(self))

    def SetGet(self, func):
        logging.debug(u"call setget path:{0} func:{1}".format(self.path, func))
        @app.route(self.path)
        def execSetGet():
            return func()

    def SetGetById(self, func):
        logging.debug(u"call setgetbyid path:{0} func:{1}".format(self.path, func))
        @app.route(self.path + '<int:id>', methods=['GET'])
        def execSetGetById(id):
            return func(id)

    def SetPost(self, func):
        logging.debug(u"call setpost path:{0} func:{1}".format(self.path, func))
        @app.route(self.path, methods=['POST'])
        def execSetPost():
            return func()

