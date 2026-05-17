# from django.test import TestCase

import json, requests

# Create your tests here.

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

# def get_resource(id=None):
#     data = {}

#     if id is not None:
#         data = {'id':id}

#     resp = requests.get(BASE_URL + END_POINT, data=json.dumps(data))  # Convert Dict 
#     print(resp.status_code)
#     print(resp.json())

# get_resource()



# def create_resource():
#     new_emp = {

#         'emp_id':3,
#         'first_name':'Aleem',
#         'last_name':'Sayyed',
#         'email':'aleem@gmail.com' ,
#         'department':'Accountant',
#         'designation':'Jr. Accountant',
#         'salary':45000,
#         'joining_date':'2026-05-17',
#         'City':'Thane',
#         'Address':'Mumbra',

#     }
#     # conver to JSON
#     resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json)

# create_resource()


def update_resource(id):    
    update_emp = {
        'id':id,
        'emp_id':4,
        'first_name':'Lambu',
        'last_name':'Bhaiya',
        'email':'lambu@gmail.com',
        'department':'JR',
        'designation':'Blinkit',
        'salary':15000,
        'joining_date':'2026-05-17',
        'City':'Mumbra',
        'Address':'MM',


    }
    resp = requests.put(BASE_URL + END_POINT, data=json.dumps(update_emp))

    print('='*30)
    print(resp.status_code)
    print(resp.json())
    print('='*30)

update_resource(3)

