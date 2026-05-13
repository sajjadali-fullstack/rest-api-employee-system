from rest_framework import serializers

from rest_framework.renderers import JSONRenderer
# JSONRenderer().render()
import io
# rest_framework ===> parsers ===> JSONParser
from rest_framework.parsers import JSONParser  # It will convert into Python Data(Dict)
# io.BytesIO(jsonData)

from testapp.models import Employee

class EmployeeSerializer(serializers.Serializer):  # 
    emp_id = serializers.IntegerField() 
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    department = serializers.CharField(max_length=100)  #EG:- IT Department
    designation = serializers.CharField(max_length=99)  # Junior Developer
    salary = serializers.DecimalField(max_digits=12, decimal_places=2)
    joining_date = serializers.DateField()
    City = serializers.CharField(max_length=55)
    Address = serializers.CharField(max_length=400)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)