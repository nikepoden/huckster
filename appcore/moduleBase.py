from appcore import app


class ModuleBase:
    def __init__(self, path):
        self.path = path
        #print "ModuleBase inited. Path:{0}".format(path)
        print
        print "Loaded module: {0}".format(self)

    def SetGet(self, func):
        print "call setget path:{0} func:{1}".format(self.path, func)
        @app.route(self.path)
        def execSetGet():
            return func()

    def SetGetById(self, func):
        print "call setgetbyid path:{0} func:{1}".format(self.path, func)
        @app.route(self.path + '<int:id>', methods=['GET'])
        def execSetGetById(id):
            return func(id)

    def SetPost(self, func):
        print "call setpost path:{0} func:{1}".format(self.path, func)
        @app.route(self.path, methods=['POST'])
        def execSetPost():
            return func()

