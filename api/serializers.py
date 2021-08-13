from rest_framework import serializers

from . import models

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Driver
        fields = '__all__'

class BusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Buses
        fields = '__all__'

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Routes
        fields = '__all__'

class BusDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BusDriver
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'

class BusRouteTimeSerializer(serializers.ModelSerializer):
    Bus_id = BusesSerializer(many=False)
    Route_id = RoutesSerializer(many=False)
    Timing = serializers.TimeField(format="%H:%M")
    class Meta:
        model = models.BusRouteTiming
        fields = '__all__'

# Nestde Serializers
class NestedBusDriverSerializer(serializers.ModelSerializer):
    Bus_id = BusesSerializer(many=False)
    Driver_id = DriverSerializer(many=False)

    class Meta:
        model = models.BusDriver
        fields = '__all__'