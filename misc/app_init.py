import import_me
from flask import Flask
import jinja2

my_loader = jinja2.FileSystemLoader(import_me.PROJECT_PATH)

def get_app(module_name):
    """ if more than one loaders are required, use this:
    loader_config = [
        app.jinja_loader,
        jinja2.FileSystemLoader('/home/chenyu/project/pinche/'),
    ]
    my_loader = jinja2.ChoiceLoader(loader_config)
    """
    app = Flask(__name__)
    app.jinja_loader = my_loader
    return app
