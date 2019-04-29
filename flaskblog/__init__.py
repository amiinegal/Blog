from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
#from flask_uploads import UploadSet,configure_uploads,IMAGES
#from flask_simplemde import SimpleMDE


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
#photos = UploadSet('photos',IMAGES)
#simple.init_app(app)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)


# setting config
    from .request import configure_request
    configure_request(app)
    # configure UploadSet
    #configure_uploads(app,photos)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
