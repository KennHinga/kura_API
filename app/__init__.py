from flask import Flask
from app.api.v1.views.views import version_one as v1

def create_app():
    """create the flask application"""
    app = Flask(__name__)
    app.register_blueprint(v1, url_prefix="/api/v1/")
    return app