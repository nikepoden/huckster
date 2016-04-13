#!flask/bin/python
from flask import Flask
from app import flask_app
import config
import modules_manager
config = config.BDProperties('config.cfg')



flask_app = Flask(__name__)
#import views
#modules_manager
# print  modules_manager.getPlugins()
# for i in modules_manager.getPlugins():
#     print("Loading plugin " + i["name"])
#     plugin = modules_manager.loadPlugin(i)
#     x = plugin.IndexPlugin(flask_app)
#     x.run1()

@flask_app.route('/qqq')
def index():
    return "123!"
flask_app.run(debug = True)