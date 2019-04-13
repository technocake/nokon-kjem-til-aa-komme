from django.contrib import admin
from .models import *

admin.site.register(Theatre)
admin.site.register(Production)
admin.site.register(Performance)
admin.site.register(Reservation)
admin.site.register(Person)
admin.site.register(Ticket)
admin.site.register(TicketType)

