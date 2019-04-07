from django.contrib import admin
from .models import Production, Performance, Reservation, Person

admin.site.register(Production)
admin.site.register(Performance)
admin.site.register(Reservation)
admin.site.register(Person)
