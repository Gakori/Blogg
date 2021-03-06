from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.loginview = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
# csrf=CSRFProtect()
mail = Mail()
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    app = Flask(__name__)
    
    
    #creating app configs
    app.config.from_object(Config)
    
    #creating the app configurations
    app.config.from_object(config_options[config_name])
    
    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    # csrf.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')
    
    #configure uploadset
    configure_uploads(app,photos)
    
    # simple.init_app(app)
    
    return app