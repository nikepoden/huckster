from moduleBase import ModuleBase

class ModuleIndex(ModuleBase):
    def __init__(self):
        print "Loaded ModuleIndex"
        ModuleBase.__init__(self, "/hello2/")
        self.SetGet(self.execPost)
        self.SetGetById(self.execGetById)
        self.SetPost(self.execPost)

    def execGet(self):
        return "exec get from dynamic module"

    def execGetById(self, id):
        return "exec get by id from dynamic module: {0}".format(id)

    def execPost(self):
        return "exec post from dynamic module"

    def init(self):
        self.SetGet(self.execPost)
        self.SetGetById(self.execGetById)
        self.SetPost(self.execPost)