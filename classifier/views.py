from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import FileSerializer
from .ml_model import classify_image


@api_view(['POST'])
def upload(request):
    serializer = FileSerializer(data=request.data)

    if serializer.is_valid():
        instance = serializer.save()

        class_name, confidence = classify_image(instance.file_input.path)

        instance.predicted_class = class_name
        instance.confidence_score = confidence
        instance.save()

        return Response(FileSerializer(instance).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)