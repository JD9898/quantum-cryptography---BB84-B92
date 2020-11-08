import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

#create an instance of Flask
app = Flask(__name__)
api = flask_restful.Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("containers.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    """Present some documentation"""

    #Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        #Read the content of the file
        content = markdown_file.read()

        #Convert to HTML
        return markdown.markdown(content)

class ContainerList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        containers = []

        for key in keys:
            containers.append(shelf[key])

        return {'message':'Success', 'data': containers}

api.add_resource(ContainerList, '/containers')
