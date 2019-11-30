import os

class Config:
    # pass
    BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass

    DEBUG = True    
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}