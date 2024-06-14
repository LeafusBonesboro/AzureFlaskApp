from flask import Flask, render_template
from flask_restful import Api

from .profiles import profiles_blueprint
from .api.profile import ProfileResource

app = Flask(__name__)
api = Api(app, prefix="/api")

app.register_blueprint(profiles_blueprint)

api.add_resource(ProfileResource, "/profiles")

@app.route("/")
def index():
    return render_template("index.html")