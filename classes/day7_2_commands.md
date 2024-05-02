## update sample_api/views.py

`
def get(self, request, id):  
        result = Students.objects.get(id=id)  
        if id:  
            serializers = StudentSerializer(result)  
            return Response({'success': 'success', "students":serializers.data}, status=200)  
  
        result = Students.objects.all()  
        serializers = StudentSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200) 
`

## update sample_api/urls.py

`
path('basic/<int:id>/', StudentView.as_view())  

`