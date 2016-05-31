from moduleBase import ModuleBase


class Module(ModuleBase):
    def __init__(self):
        ModuleBase.__init__(self, "/hello/")
        self.SetGet(self.execPost)
        self.SetGetById(self.execGetById)
        self.SetPost(self.execPost)

    def execGet(self):
        return "exec get"

    def execGetById(self, id):
        return "exec get by id: {0}".format(id)

    def execPost(self):
        return "exec post"