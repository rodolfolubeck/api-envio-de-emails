import markdown
import os
import shelve

from flask import Flask, g
from flask_restful import Resource, Api, reqparse
from .contact import Contact

app = Flask(__name__)

api = Api(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("email_trigger.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)


class SentList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        sentList = []

        for key in keys:
            sentList.append(shelf[key])

        return {'message': 'Success', 'data': sentList}, 200


class Send(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('sendDate', required=True)

        args = parser.parse_args()

        contact = Contact(args['identifier'], args['email'], args['name'], args['sendDate'])
        contact.send_email(args['email'])

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'E-mail sent', 'data': args}, 201


class EmailSent(Resource):
    def get(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message': 'E-mail not found', 'data': {}}, 404

        return {'message': 'E-mail found', 'data': shelf[identifier]}, 200


api.add_resource(SentList, '/sent')
api.add_resource(Send, '/send')
api.add_resource(EmailSent, '/sent/<string:identifier>')