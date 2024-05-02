## run command:

`
pip install djangorestframework

python manage.py startapp sample_api
`

## add settings.py

`
'rest_framework',  
    'sample_api', 

`

## update sample_api/models.py

`
 
class Students(models.Model):  
    first_name = models.CharField(max_length=200)  
    last_name = models.CharField(max_length=200)  
    address = models.CharField(max_length=200)  
    roll_number = models.IntegerField()  
    mobile = models.CharField(max_length=10)  
  
    def __str__(self):  
        return self.first_name + " " + self.last_name  
`

## update sample_api/admin.py

`
from .models import Students  
  
# Register your models here.  
admin.site.register(Students)
`

## run command:

`
python3 manage.py makemigrations  
python3 manage.py migrate 
`

## create file sample_api/serializers.py

`

from rest_framework import serializers  
from .models import Students  
  
class StudentSerializer(serializers.ModelSerializer):  
    first_name = serializers.CharField(max_length=200, required=True)  
    last_name = serializers.CharField(max_length=200, required=True)  
    address = serializers.CharField(max_length=200, required=True)  
    roll_number = serializers.IntegerField()  
    mobile = serializers.CharField(max_length=10, required=True)  
  
    class Meta:  
        model = Students  
        fields = ('__all__') 

    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Students.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Students` instance, given the validated data. 
        """  
        instance.first_name = validated_data.get('first_name', instance.first_name)  
        instance.last_name = validated_data.get('last_name', instance.last_name)  
        instance.address = validated_data.get('address', instance.address)  
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)  
        instance.mobile = validated_data.get('mobile', instance.mobile)  
  
        instance.save()  
        return instance 
`

## update sample_api/views.py

`

from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Students  
from .serializers import StudentSerializer  
# Create your views here.  
  
class StudentView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Students.objects.all()  
        serializers = StudentSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = StudentSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

`

## add blogs/urls.py

` 
path('api/', include('sample_api.urls')),
`



## create sample_api/urls.py

`

from .views import StudentView  
from django.urls import path  
  
urlpattern = [  
    path('basic/', StudentView.as_view())  
]  

`

290


