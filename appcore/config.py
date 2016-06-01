import os
from ConfigParser import SafeConfigParser

class BDProperties:
        def __init__(self, fname):
                self.filename = (os.path.join(os.getcwd(),fname))
                self.cfgParser = SafeConfigParser()
                self.load()
        def load(self):
                self.cfgParser.read(self.filename)
        def getDbConnectionString(self):
                return self.cfgParser.get('database_connection', 'url');
        def getLogin(self):
                return self.cfgParser.get('database_connection','username');
        def getPass(self):
                return self.cfgParser.get('database_connection','password');
        def getModulesDir(self):
                return self.cfgParser.get('modules','modulesdir');