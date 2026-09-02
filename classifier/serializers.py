from rest_framework import serializers
from .models import MachineLearningModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineLearningModel
        fields = '__all__'
        read_only_fields = ('predicted_class', 'confidence_score','timestamp')


class MachineLearningModelSerializer:
    pass