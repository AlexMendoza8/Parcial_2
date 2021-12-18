from flask import Flask


def create_app():
    flask_app = Flask(__name__)
    
    # make flask app
    from .views import views

    flask_app.register_blueprint(views, url_prefix='/')
    
    return flask_app

    

