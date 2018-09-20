from django.shortcuts import render
from bidtool.models import *
from bidtool.forms import *
# Create your views here.

def home(request):
    embassies = Embassy.objects.all()
    if request.method=='GET':
        if 'name' in request.GET:
            embassies = embassies.filter(name__icontains=request.GET['name'])
    return render(request, 'home.html', context={'embassies':embassies, 'form': embassySearch})