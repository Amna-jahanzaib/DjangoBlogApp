from django.contrib import admin

# Register your models here.
from .models import Flights,Airport,Passenger

class PassengerInAirline(admin.StackedInline):
    model=Passenger.flights.through
    extra=1

class FlightsAdmin(admin.ModelAdmin):
    inline=[PassengerInAirline]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)


admin.site.register(Airport)
admin.site.register(Flights,FlightsAdmin)
admin.site.register(Passenger,PassengerAdmin)

