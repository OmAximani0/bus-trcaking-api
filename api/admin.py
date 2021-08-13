from django.contrib import admin

from . import models

admin.site.register(models.Driver)
admin.site.register(models.Buses)
admin.site.register(models.Routes)
admin.site.register(models.BusDriver)
admin.site.register(models.Location)
admin.site.register(models.BusRouteTiming)