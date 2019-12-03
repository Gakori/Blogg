import os

class Config:
    # pass
    
    SECRET_KEY=os.environ.get('SECRET_KEY')
    BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
     
     #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'BLOGG'
    SENDER_EMAIL = 'faithgakori506@gmail.com'
    
class ProdConfig(Config):
    # pass
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    # pass
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://faith:456789@localhost/blogg'
    
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}