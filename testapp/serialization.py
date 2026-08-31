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

    # Create Data
    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)

    # Update Data
    def update(self, instance, validated_data):
        instance.emp_id = validated_data.get('emp_id',instance.emp_id)
        instance.first_name = validated_data.get('first_name',instance.first_name) 
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.department = validated_data.get('department',instance.department)
        instance.designation = validated_data.get('designation',instance.designation)
        instance.salary = validated_data.get('salary',instance.salary)
        instance.joining_date = validated_data.get('joining_date',instance.joining_date)
        instance.City = validated_data.get('City',instance.City)
        instance.Address = validated_data.get('Adress',instance.Address)

        instance.save()
        return instance



# Validate Data

    # def validate_salary(self,value):
    #     if value < 40000:
    #         raise serializers.ValidationError("Employee Salary Should be 4000")
    #     return value

    
# 2. Partial update for Object level  Validate with name     
    def validate(self, data):
        first_name = data.get('first_name') 
        salary = data.get('salary')
        
        if first_name.lower() == 'amir':
            if salary < 90000:
                raise serializers.ValidationError("Amir Salary should be 90K / more")
        return data
