from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from testapp.models import Employee
from testapp.serialization import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your business logic / views here 👇.


# 1. Partner Application nothing but test.py  want all Employee records in JSON formet.

# qurey set ===> python native dataType(serialization)
#     python native data type ===> JSON data(JSONRenderer().render())

# class EmployeeCRUDCVB(View):
    
#     def get(self, request, *args, **kwargs):        
#         # Data from the Body
#         json_data = request.body
#         # Convert into Stream
#         stream = io.BytesIO(json_data)
#         # JSON data to Python Data
#         pdata = JSONParser().parse(stream)

#         id = pdata.get('id', None)
        
#         if id is not None:
#             emp = Employee.objects.get(id=id)  # Comple Type
#             eserializer = EmployeeSerializer(emp)
#             # Convert into JSON data
#             json_data = JSONRenderer().render(eserializer.data)

#             return HttpResponse(json_data, content_type='application/json', status=200)
#         # if not come than this 
#         qurey_set = Employee.objects.all()
#         eserializer = EmployeeSerializer(qurey_set, many=True)
#         json_data = JSONRenderer().render(eserializer.data)
#         return HttpResponse(json_data, content_type='application/json', status=200)



@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View):

    # def post(self, request, *args, **kwargs):

    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pdata = JSONParser().parse(stream)
    #     serializer = EmployeeSerializer(data=pdata)

    #     if serializer.is_valid():
    #         serializer.save()
    #         msg = {'msg':'Resources created sucessfully '}
    #         json_data = JSONRenderer().render(msg)
    #         return HttpResponse(json_data, content_type='application/json')
    
    #     # print Error
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='appplication/json', status=400)

    def put(self, request, *args, **kwargs):
        # Collect the data
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=pydata)

        if serializer.is_valid():
            serializer.save()

            msg = {'msg':'Resources updated sucessfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)




