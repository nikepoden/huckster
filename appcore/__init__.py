import config
from flask import Flask


app = Flask(__name__)
config = config.BDProperties('config.cfg')
from appcore import views