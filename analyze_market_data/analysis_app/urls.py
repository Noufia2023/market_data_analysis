from django.urls import path
from .views import AnalyzeSectorView



urlpatterns = [
    path('analyze/<str:sector>/', AnalyzeSectorView.as_view(), name='analyze-sector'),
]

