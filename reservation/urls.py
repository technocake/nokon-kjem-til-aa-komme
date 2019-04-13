from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Reservasjons api
router.register(r'theatre', TheatreViewSet)
router.register(r'productions', ProductionViewSet)
router.register(r'performances', PerformanceViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'ticket_types', TicketTypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('swagger', get_swagger_view(title='BillettReservasjons API'))
]
