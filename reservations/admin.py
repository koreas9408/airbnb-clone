from django.contrib import admin
from . import models

@admin.register(models.Resrvation)
class ReservationAdmin(admin.ModelAdmin):

    """ Resrvation Model Admin Definition """
    pass
