from django.shortcuts import render
from .serializers import MachineLearningModelSerializer
from .models import MachineLearningModel

@api_view(['GET'])
def file_get(request, format=None):
    

