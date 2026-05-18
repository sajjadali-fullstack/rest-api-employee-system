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



# CREATE RESOURCE
def create_resource():
    new_emp = {

        'emp_id':9,
        'first_name':'Aleem',
        'last_name':'Sayyed',
        'email':'aleemcc@gmail.com' ,
        'department':'Accountant',
        'designation':'Jr. Accountant',
        'salary':450000,
        'joining_date':'2026-05-17',
        'City':'Thane',
        'Address':'Mumbra Kausa',

    }
    # conver to JSON
    resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json)

create_resource()


#                                        UPDATE RESOURCE


# BASE_URL = 'http://127.0.0.1:8000/'
# END_POINT = 'api-update/'
# def update_resource(id):    
#     update_emp = {
#         'id':id,
#         'emp_id':3,
#         'first_name':'Lambu',
#         'last_name':'Bhaiya',
#         'email':'lambu@gmail.com',
#         'department':'JR',
#         'designation':'Blinkit',
#         'salary':15000,
#         'joining_date':'2026-05-17',
#         'City':'Mumbra',
#         'Address':'MM',


#     }
#     resp = requests.put(BASE_URL + END_POINT, data=json.dumps(update_emp))

#     print('='*40)

#     print(resp.status_code)  # 200
#     print(resp.json())  # {'msg': 'Resources updated sucessfully'}
    
#     print('='*40)


# update_resource(2)




print()
print('**'*40)
print()




#                                      Partial Update


# BASE_URL = 'http://127.0.0.1:8000/'
# END_POINT = 'api-partial-update/'
# def partial_resource(id):
#     partial_emp = {
#         'id':id,
#         'first_name':'Ronu',
#     }
#     resp = requests.put(BASE_URL + END_POINT, data=json.dumps(partial_emp))
#     print(resp.status_code)
#     print(resp.json())


# partial_resource(2)


# print()
# print('~'*40)
# print()


                # DELETE the resource

# BASE_URL = 'http://127.0.0.1:8000/'
# END_POINT = 'api-delete/'


# def delete_resource(id):
#     data = {
    
#         'id':id
#     }
#     resp = requests.delete(BASE_URL + END_POINT, data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())

# delete_resource(6)    