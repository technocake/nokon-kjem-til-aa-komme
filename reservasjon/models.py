# coding: utf-8
from django.db import models


class CreatedUpdatedModel(models.Model):
    """
        Add created_at and updated_at fields to all inheriting models.

        Got lots of pointers here:
        https://medium.com/@zmudzinski/create-a-basemodel-in-django-a7ca297cef62
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_index=True
    )

    class Meta:
        abstract = True


class Person(CreatedUpdatedModel):
    """
        Dude holding a reservation or beeing reserved for.
    """
    name = models.CharField(max_length=512, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Performance(CreatedUpdatedModel):
    """
        A performance of a production
    """
    seats = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)

    def __str__(self):
        return self.start.strftime("%d.%m %H:%M")


class Reservation(CreatedUpdatedModel):
    """
        A reservation for a performance
    """
    reserved_by = models.ForeignKey(Person, related_name='reserved_by', on_delete=models.CASCADE)  # noqa
    reserved_for = models.ManyToManyField(Person, related_name='reserved_for')  # noqa
    performance = models.ForeignKey(Performance, related_name='reservations', on_delete=models.CASCADE)  # noqa

    @property
    def number_of_seats(self):
        """ Gets the number of seats in this reservation,
            by counting people reserved for.
        """
        return self.reserved_for.count()

    def __str__(self):
        return "{} seats on {} for {}".format(
            self.number_of_seats,
            self.performance,
            self.performance.production.name
        )


class Production(CreatedUpdatedModel):
    """
        Theater production, contains performances
    """
    name = models.CharField(max_length=512)
    description = models.TextField()
    performances = models.ManyToManyField(Performance, related_name='production')  # noqa

    def __str__(self):
        return self.name

