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
    route=list(AirportRoute.objects.all().order_by('airport_code'))
    return render(request, 'routes/add_route.html', {'form': form, 'route':route})  #pass the form value add_route.html



def longest_route(request):
    route = AirportRoute.objects.order_by('-duration').first()  #sort by asc and get the first one
    return render(request, 'routes/longest.html', {'route': route}) #pass the first to longest.html



def search_node(request):
    result = None
    error = None
    if request.method == "POST":
        n = int(request.POST.get("n")) #get n from form
        direction = request.POST.get("direction") #get the direction left or right

        # Step 1: Get all routes ordered by position and store in array
        routes = list(AirportRoute.objects.all().order_by('position'))

        # Step 2: Reverse if right
        if direction == "right":
            routes.reverse()

        # Step 3: Get nth node
        if 0 < n <= len(routes):
            result = routes[n - 1]
        else:
            error = "N value doesnt exist. Please enter a valid number." #to give err msg

    return render(request, 'routes/search.html', {'result': result,'error':error})



def shortest_between(request):
    result = None

    if request.method == "POST":
        start = int(request.POST.get("start"))
        end = int(request.POST.get("end"))

        # Step 1: Filter range position>=start and position<=end
        routes = AirportRoute.objects.filter(
            position__gte=start,
            position__lte=end
        )

        # Step 2: Find minimum duration
        result = routes.order_by('duration').first()

    return render(request, 'routes/shortest.html', {'result': result})