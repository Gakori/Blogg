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

    # with urllib.request.urlopen(base_url) as url:
    #     data=url.read()
    #     response=json.loads(data)
        
    #     results=process_quote(response)
    #     print('results')
    
    data = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    response = data.json()
    results = response
    print(results)

    return results

# def process_quote(item):
#     '''
#     function that processess the movie results
    
#     Args:
#         item:
#             contains quotes
#         Returns:
#             quote_results:quotes objects
#     '''
#     results=[]
    
#     author=item.get('author')
#     quote=item.get('quote')
    
#     quote_object=Quote(author,quote)
#     results.append(quote_object)
    
#     return results
        
        
        
        
   