# coding: utf-8
from django.db import models
from .common import CreatedUpdatedModel, Person, TicketType
from .shows import Reservation


class Ticket(CreatedUpdatedModel):
    """
        A ticket, for a given show (performance)
        and for a given person
        of a given TicketType
    """
    reservation = models.ForeignKey(Reservation,
                                    related_name='tickets',
                                    on_delete=models.CASCADE)  # noqa

    type = models.ForeignKey(TicketType,
                             # don't create reverse field on TicketType class
                             related_name='+',
                             null=True,
                             on_delete=models.CASCADE)

    holder = models.ForeignKey(Person,
                               related_name='tickets',
                               null=True,
                               on_delete=models.CASCADE)

    picked_up = models.BooleanField(default=False)
