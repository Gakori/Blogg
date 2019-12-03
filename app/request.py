# import urllib.request,json
from .models import Quote
import  requests

base_url = None

def configure_request(app):
    global base_url
    
    base_url = app.config['BASE_URL']

def get_quotes():
    '''
    function that gets the json response to url request
    '''
    data = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    response = data.json()
    results = response
    print(results)

    return results


        
        
        
        
   