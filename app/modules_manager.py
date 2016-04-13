import imp
import os

ModuleFolder = (os.path.join(os.getcwd(),'modules'))
MainModule = "__init__"

def getPlugins():
    modules = []
    possibleplugins = os.listdir(ModuleFolder)
    for i in possibleplugins:
        location = os.path.join(ModuleFolder, i)
        if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
            continue
        info = imp.find_module(MainModule, [location])
        modules.append({"name": i, "info": info})
    return modules

def loadPlugin(module):
    return imp.load_module(MainModule, *module["info"])