from django.shortcuts import HttpResponse
from django.template import loader

def display(request):
    template = loader.get_template('connect_settlement/this_month.html')
    return HttpResponse(template.render())
    # return HttpResponse("hogehogwe")
