from django.shortcuts import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Equipment



def index(request):
    equipments = Equipment.objects.order_by('equipment_amount')[0:]
    context = {
        'equipment_list': Equipment.objects.all(), 
    }
    return render(request, 'equipment_database/index.html', context)

# class DatabaseView(generic.DateDetailView):
    # def get_queryset(self):
    #     return Equipment.objects.order_by('equipment_name')
    # template_name = '../equipment_database/' 