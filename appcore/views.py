from appcore import app
import modules_manager

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

from moduleCore import Module
x = Module()
loadedModules = []

#modules_manager
#print  modules_manager.getPlugins()
print "autoload"
for i in modules_manager.getPlugins():
     #print("Loading plugin " + i["name"])
     plugin = modules_manager.loadPlugin(i)
     #m = plugin.__init__(i["name"])
     print plugin

     #plugin.init()

     #plugin.__init__("ModuleIndex")
     #m = plugin()
     #my_class = getattr(m, "")
     #instance = my_class()
     #loadedModules.append(m)
print "autoload finished"