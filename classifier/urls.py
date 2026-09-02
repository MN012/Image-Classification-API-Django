from django.urls import path
from .views import upload

urlpatterns = [
    path('classify/', upload, name='classify-image'),
]