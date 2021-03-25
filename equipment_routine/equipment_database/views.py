from django.shortcuts import HttpResponse
from django.views import generic
from django.template import loader

from .models import Equipment

def index(request):
    template = loader.get_template('equipment_database/index.html')
    return HttpResponse(template.render())

# class DatabaseView(generic.DateDetailView):
    # def get_queryset(self):
    #     return Equipment.objects.order_by('equipment_name')
    # template_name = '../equipment_database/' 