from moduleBase import ModuleBase
from flask import abort, jsonify, request
import logging

def GetModuleInstance():
    return ModuleComment()

comments = [
    {
        'id': 1,
        'id_item': u'1234',
        'author': u'Vasya',
        'message': u'Message1'
    },
    {
        'id': 2,
        'id_item': u'1234',
        'author': u'Sergey',
        'message': u'Message2'
    }
]

class ModuleComment(ModuleBase):
    def __init__(self):
        ModuleBase.__init__(self, "/comment/")
        self.SetGet(self.execGet)
        self.SetGetById(self.execGetById)
        self.SetPost(self.execPost)
        logging.debug(u"Loaded module: {0}".format(self))

    def execGet(self):
        return jsonify({'messages': comments})

    def execGetById(self, id):
        message = filter(lambda t: t['id'] == id, comments)
        if len(message) == 0:
            abort(404)
        return jsonify({'messages': comments[0]})

    def execPost(self):
        print request.json
        if not request.json: #or not 'title' in request.json:
           abort(400)
        comment = {
            'id': comments[-1]['id'] + 1,
            'id_item': request.json['id_item'],
            'author': request.json.get('author', ""),
            'message': request.json.get('message', "")
        }
        comments.append(comment);
        return jsonify({'message': comment}), 201
        #return "exec post from dynamic module"

    def init(self):
        self.SetGet(self.execPost)
        self.SetGetById(self.execGetById)
        self.SetPost(self.execPost)