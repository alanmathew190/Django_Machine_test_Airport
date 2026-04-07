from django.shortcuts import render, redirect
from .models import AirportRoute
from .form import AirportRouteForm

def add_route(request):
    if request.method == "POST":
        form = AirportRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_route')
    else:
        form = AirportRouteForm()

    return render(request, 'routes/add_route.html', {'form': form})
