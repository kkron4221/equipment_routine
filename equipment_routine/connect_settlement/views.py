from django.shortcuts import HttpResponse

def display(request):
    return HttpResponse("Main Display.")
