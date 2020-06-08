import logging
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import azure.functions as func
from math import radians, sin, cos, asin, sqrt
import requests
  
# api-endpoint
URL = "https://locustlocater-e46b6.firebaseio.com/.json"

  
# location given here

  
# defining a params dict for the parameters to be sent to the API

  
# sending get request and saving the response as response objpychpppppuppppr = requests.get(url = URL)
  
# extracting data in json format
data = r.json()



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return (str(data))
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
