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


class TicketType(CreatedUpdatedModel):
    """
        Representation of ticket types.
        Student ticket, ordinary etc.
    """
    name = models.CharField(max_length=255)
    price = models.IntegerField()