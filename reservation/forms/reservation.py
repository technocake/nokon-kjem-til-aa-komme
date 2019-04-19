from django import forms
from ..models import Reservation


class ReservationForm(forms.ModelForm):
    """ The form to rule them all """

    class Meta():
        fields = (
            'reserved_by',
            'performance',
            'number_of_tickets',
        )
        model = Reservation
