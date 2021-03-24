from django.urls import path

from . import views

urlpatterns = [
    path('', views.DatabaseView.as_view(), name='index'),
]