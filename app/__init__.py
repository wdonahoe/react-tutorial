from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app.views import view as view_module

app.register_blueprint(view_module)
