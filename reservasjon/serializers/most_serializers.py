from rest_framework import routers, serializers, viewsets

from django.contrib.auth.models import User
from ..models import Production, Performance, Reservation, Person


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ProductionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Production
        fields = ('__all__')


class PerformanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Performance
        fields = ('__all__')

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ('__all__')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')    