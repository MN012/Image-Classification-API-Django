from django.db import models
from django.utils import timezone


class MachineLearningModel(models.Model):
    file_input = models.ImageField(upload_to='uploads/')
    predicted_class = models.TextField()
    confidence_score = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.predicted_class} ({self.timestamp})"