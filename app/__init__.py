from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

bootstrap = Bootstrap()
db = SQLAlchemy()
csrf=CSRFProtect()

def create_app(config_name):
    app = Flask(__name__)
    
    #creating app configs
    app.config.from_object(Config)
    app.config['SECRET_KEY'] ='vvasdbbbheh'
    
    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    csrf.init_app(app)
    
    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app

# from app import views