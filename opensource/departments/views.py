from django.shortcuts import render
from django.http import HttpResponse

import departments


# Create your views here.


def landing(request):
    # return HttpResponse("Landing Page")
    return render(request, 'departments/index.html')


# each url needs a view ?? to handle the request

def index(request):
    departments = [
        {
            "id":1,
            "name":"Opensource",
            "description":"DevTrack",
        },
        {
            "id":2,
            "name":"AI",
            'description':'AI',
        }
    ]
    return render(request, 'departments/index.html', context={'departments': departments})