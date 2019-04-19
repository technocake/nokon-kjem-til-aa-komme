# coding: utf-8
from django.db import models
from .common import CreatedUpdatedModel, Person, TicketType

# https://docs.djangoproject.com/en/2.2/ref/models/expressions/#f-expressions
from django.db.models import F


class Theatre(CreatedUpdatedModel):
    """ A theatre. Holding a set of ticket_types commonly used for
    this theatre. Produtions might overwrite those.
    """
    name = models.CharField(max_length=512)
    ticket_types = models.ManyToManyField(TicketType, related_name='theatre')  # noqa


class Production(CreatedUpdatedModel):
    """
        Theater production, contains performances
    """
    name = models.CharField(max_length=512)
    description = models.TextField()
    theatre = models.ForeignKey(Theatre, related_name='productions', on_delete=models.CASCADE)
    ticket_types = models.ManyToManyField(TicketType,
        related_name='production',
        help_text='Hvilke type billetter som selges i denne produksjonen',
        limit_choices_to={'theatre': F('theatre')},
        blank=True)  # noqa

    def __str__(self):
        return self.name


class Performance(CreatedUpdatedModel):
    """
        A performance of a production
    """
    seats = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    production = models.ForeignKey(Production, related_name='performances', on_delete=models.CASCADE)  # noqa
    ticket_types = models.ManyToManyField(TicketType, related_name='performance', blank=True)  # noqa

    def __str__(self):
        return self.start.strftime("%d.%m %H:%M")


class Reservation(CreatedUpdatedModel):
    """
        A reservation for a performance
    """
    reserved_by = models.ForeignKey(Person, related_name='reserved_by', on_delete=models.CASCADE)  # noqa
    performance = models.ForeignKey(Performance, related_name='reservations', on_delete=models.CASCADE)  # noqa
    number_of_tickets = models.IntegerField()

    def __str__(self):
        return "{} seats on {} for {}".format(
            self.number_of_tickets,
            self.performance,
            self.reserved_by
        )


