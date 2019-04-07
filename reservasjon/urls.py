from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .views import UserViewSet, ProductionViewSet, PerformanceViewSet, ReservationViewSet, PersonViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Reservasjons api
router.register(r'productions', ProductionViewSet)
router.register(r'performances', PerformanceViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'persons', PersonViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('swagger', get_swagger_view(title='BillettReservasjons API'))
]
