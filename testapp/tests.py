# from django.test import TestCase

import json, requests

# Create your tests here.

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

def get_resource(id=None):
    data = {}

    if id is not None:
        data = {'id':id}

    resp = requests.get(BASE_URL + END_POINT, data=json.dumps(data))  # Convert Dict 
    print(resp.status_code)
    print(resp.json())

get_resource()
