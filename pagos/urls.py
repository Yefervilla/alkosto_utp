from django.urls import path
from . import views

app_name = 'pagos'

urlpatterns = [
    path('', views.lista_pagos, name='pagos'),
    path('webhooks/', views.lista_webhooks, name='webhooks'),
]