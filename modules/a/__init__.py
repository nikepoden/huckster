from flask import abort, jsonify, request


class IndexPlugin:
    def __init__(self, flask_app):
        self.fapp = flask_app
    def run1(self):
        print 'A is runing'
        self.fapp.route('/')
        self.fapp.route('/index')
        def index():
            print 'Hello a!'
            #return "Hello, World!"