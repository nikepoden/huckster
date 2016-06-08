import config
from flask import Flask

config = config.BDProperties('config.cfg')

import logging
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG, filename=u'log.log')
logging.info("Application started")

app = Flask(__name__)

from appcore import views