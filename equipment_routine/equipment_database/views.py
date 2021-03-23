from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("First Test with making apps")