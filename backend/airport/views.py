from django.shortcuts import render, redirect
from .models import AirportRoute
from .form import AirportRouteForm

def add_route(request):
    if request.method == "POST":  
        form = AirportRouteForm(request.POST)    #import form skeleton
        if form.is_valid():  #check valid
            form.save()
            return redirect('add_route')  # redirected to again add route 
    else:
        form = AirportRouteForm()

    return render(request, 'routes/add_route.html', {'form': form})  #pass the form value add_route.html


def longest_route(request):
    route = AirportRoute.objects.order_by('-duration').first()  #sort by asc and get the first one
    return render(request, 'routes/longest.html', {'route': route}) #pass the first to longest.html

