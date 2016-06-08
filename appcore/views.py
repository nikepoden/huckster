from appcore import app
import logging
import modules_manager

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

from moduleCore import Module
x = Module()
loadedModules = []

logging.debug(u"autoload modules")
for i in modules_manager.getPlugins():
     #print("Loading plugin " + i["name"])
     plugin = modules_manager.loadPlugin(i)
     x = plugin.GetModuleInstance()
     loadedModules.append(x)
     #print plugin
logging.debug(u"autoload modules finished")