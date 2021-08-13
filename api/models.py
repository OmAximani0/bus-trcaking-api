from django.db import models

# Tabel = 'driver'
class Driver(models.Model):
    Driver_id = models.AutoField(primary_key=True)
    Driver_name = models.CharField(max_length=100, null=False, blank=False)
    Driver_phone = models.CharField(max_length=10, null=False, unique=True, blank=False)

    class Meta:
        db_table = 'driver'
        verbose_name_plural = 'drivers'

    def __str__(self):
        return self.Driver_name

# Tabel = 'buses'
class Buses(models.Model):
    Bus_id = models.AutoField(primary_key=True)
    Bus_number = models.CharField(max_length=20, unique=True, null=False, blank=False)
    Bus_name = models.CharField(max_length=30, null=False)

    class Meta:
        db_table = 'buses'
    
    def __str__(self):
        return self.Bus_name

# Tabel = 'routes'
class Routes(models.Model):
    Route_id = models.AutoField(primary_key=True)
    Route_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'routes'

    def __str__(self):
        return self.Route_name

# Tabel = 'bus_driver'
class BusDriver(models.Model):
    Bus_id = models.ForeignKey(Buses, on_delete=models.CASCADE)
    Driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)

    class Meta:
        db_table = 'bus_driver'

# Tabel = 'location'
class Location(models.Model):
    Location_id = models.AutoField(primary_key=True)
    Bus_id = models.ForeignKey(Buses, on_delete=models.CASCADE)
    Lat = models.CharField(max_length=50, null=False)
    Long = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'location'

# Tabel = 'bus_route_timing'
class BusRouteTiming(models.Model):
    Bus_id = models.ForeignKey(Buses, on_delete=models.CASCADE)
    Route_id = models.ForeignKey(Routes, on_delete=models.CASCADE)
    Timing = models.TimeField()

    class Meta:
        db_table = 'bus_route_timing'