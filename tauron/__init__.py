from flask import Flask
from flask_login import LoginManager
from .routes import main
from .auth import auth
from .models import User


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yZas1@3lsssdx'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):

      return User(user_id)


    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
