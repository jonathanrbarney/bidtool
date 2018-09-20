from django.shortcuts import render
from bidtool.models import *
from bidtool.forms import *
from itertools import chain
# Create your views here.

def home(request):
    embassies = Embassy.objects.all()
    selected=[]
    if request.method=='GET':
        if 'country' in request.GET:
            selected = request.GET.getlist('country')
            embassies=embassies.filter(long_country__in=selected)
        if 'name' in request.GET:
            if request.GET.get('name') != '':
                embassies = embassies.filter(name__icontains=request.GET.get('name'))

        locs = Embassy.objects.order_by().values('long_country').distinct()
        countries=[]
        for i in locs:
            countries.append(i['long_country'])
    return render(request, 'home.html', context={'embassies':embassies, 'form': embassySearch, 'countries':countries, 'selected':selected})