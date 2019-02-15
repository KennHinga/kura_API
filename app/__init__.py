from flask import Flask
from app.api.v1.views.views import version_one as v1
from app.api.v2.Views.user_views import version_two as v2

def create_app(config_name):
    """create the flask application"""
    app = Flask(__name__)
    app.register_blueprint(v1, url_prefix="/api/v1/")
    app.register_blueprint(v2, url_prefix="/api/v2/")
    # app.url_map,strict_slashes = False
    return app