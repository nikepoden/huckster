from appcore import app


class ModuleBase:
    def __init__(self, path):
        self.path = path
        print "ModuleBase inited. Path:{0}".format(path)

    def SetGet(self, func):
        print "call setget"
        @app.route(self.path, methods=['GET'])
        def execSetGet():
            return func()

    def SetGetById(self, func):
        print "call setgetbyid"
        @app.route(self.path + '<int:id>', methods=['GET'])
        def execSetGetById(id):
            return func(id)

    def SetPost(self, func):
        print "call setpost"
        @app.route(self.path, methods=['POST'])
        def execSetPost():
            return func()

