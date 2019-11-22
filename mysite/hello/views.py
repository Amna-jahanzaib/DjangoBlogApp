from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from .models import Flights, Passenger
def index(request):
    context={
        "flights": Flights.objects.all()
    }
    return render(request,"flights/index.html",context)
def flight(request,flight_id):
    try:
        flight=Flights.objects.get(pk=flight_id)
    except Flights.DoesNotExist:
        raise Http404("Flight does not Exist")
    context={
        "flight": flight,
        "passengers":flight.passengers.all(),
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flight.html",context)

def book(request,flight_id):
    try:
        passenger_id=int(request.POST["passenger"])
        flight=Flights.objects.get(pk=flight_id)
        passenger=Passenger.objects.get(pk=passenger_id)
    except KeyError:
        return render(request, "flights/error.html",{"message":"No Selection"})
    except passenger.DoesNotExist:
            return render(request, "flights/error.html",{"message":"Passenger does not Exist"})
    except flight.DoesNotExist:
            return render(request, "flights/error.html",{"message":"Flight does not Exist"})
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight",args=(flight_id,)))
