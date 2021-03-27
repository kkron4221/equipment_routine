from django.urls import path

from . import views

app_name = 'connect_settlement'

urlpatterns = [
    path('', views.display, name='display'),
]