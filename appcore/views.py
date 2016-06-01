from appcore import app
import modules_manager

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

from moduleCore import Module
x = Module()
loadedModules = []

print "autoload"
for i in modules_manager.getPlugins():
     #print("Loading plugin " + i["name"])
     plugin = modules_manager.loadPlugin(i)
     x = plugin.GetModuleInstance()
     loadedModules.append(x)
     #print plugin
print "autoload finished"