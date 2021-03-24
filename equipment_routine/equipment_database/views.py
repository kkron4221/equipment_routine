from django.shortcuts import HttpResponse
from django.views import generic

from .models import Equipment

class DatabaseView(generic.DateDetailView):
    def get_queryset(self):
        return Equipment.objects.order_by('equipment_name')
    template_name = '../equipment_database/' 