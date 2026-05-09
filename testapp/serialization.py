from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):  # 
    emp_id = serializers.IntegerField() 
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    department = serializers.CharField(max_length=100)  #EG:- IT Department
    designation = serializers.CharField(max_length=99)  # Junior Developer
    salary = serializers.DecimalField(max_digits=12, decimal_places=2)
    joining_date = serializers.DateField()
    emp_name = serializers.CharField(max_length=88)
    emp_sal = serializers.FloatField()
    emp_addr = serializers.CharField(max_lengt=400)