from django.urls import path
from .views import AnalyzerView

urlpatterns = [
    path("/home", AnalyzerView.as_view(), name='image-analyzer'),
]
