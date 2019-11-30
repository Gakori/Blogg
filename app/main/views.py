from flask import render_template
from . import main
from flask_login import login_required
# from app import app
from app import db
from app.main import main
# from ..request import get_quotes

@main.route('/')
def index():
    '''
    view root page function that returns index and its data 
    '''
    # quote = get_quotes()
    
    return render_template('index.html')
