from django.contrib import admin
from .models import *

admin.site.register(Performance)
admin.site.register(Reservation)
admin.site.register(Person)
admin.site.register(Ticket)
admin.site.register(TicketType)


class TicketTypeUXModelAdmin(admin.ModelAdmin):
    """
    Adds common widget logic in this class,
    for all models having a ticket_type field.
    Adds better ux to the ticket_types fields
    """
    filter_horizontal = ['ticket_types']


class PerformanceInline(admin.TabularInline):
    """
    Makes it possible to set
    performances on a production from admin.
    """
    model = Performance
    exclude = ['ticket_types']


@admin.register(Production)
class ProductionAdmin(TicketTypeUXModelAdmin):
    """
    Django admin humbug to make us able
    to set performances directly on the
    production admin page.
    """
    inlines = [
        PerformanceInline
    ]


@admin.register(Theatre)
class TheatreAdmin(TicketTypeUXModelAdmin):
    pass
