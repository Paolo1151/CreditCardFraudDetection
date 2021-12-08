from django.urls import path

from . import views

urlpatterns = [
    path('', views.fraud_detection, name='Fraud Detection')
]
