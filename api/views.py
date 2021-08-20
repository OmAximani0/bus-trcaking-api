from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from datetime import datetime

from . import models
from . import serializers

class AllRoutes(generics.ListAPIView):
    queryset = models.Routes.objects.all()
    serializer_class = serializers.RoutesSerializer

class ViewLocations(APIView):
    def post(self, request):
        Bus_id = request.data['Bus_id']
        instance = models.Location.objects.filter(Bus_id=Bus_id).order_by('-Location_id')[0]
        serializer = serializers.LocationSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddLocation(APIView):
    def post(self, request):
        response = {}
        serializer = serializers.LocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response['msg'] = "Location Added!"
            return Response(response, status=status.HTTP_201_CREATED)
        response['msg'] = serializer.error_messages
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class ViewBuses(APIView):
    def post(self, request):
        response = []
        Time = datetime.now().time()
        Route_id = request.data['Route_id']
        print(Time)
        route_instance = models.BusRouteTiming.objects.filter(Route_id=Route_id, Timing__gte=Time)
        print(route_instance)
        bus_route_serializer = serializers.BusRouteTimeSerializer(route_instance, many=True)
        temp_dict = {}
        for data in bus_route_serializer.data:
            print(data)
            Bus_id = data.get('Bus_id')['Bus_id']
            temp_dict['Bus_id'] = Bus_id
            temp_dict['Bus_name'] = data.get('Bus_id')['Bus_name']
            temp_dict['Bus_number'] = data.get('Bus_id')['Bus_number']
            temp_dict['Route_name'] = data.get('Route_id')['Route_name']
            temp_dict['Time'] = data.get('Timing')
            bus_driver_instance = models.BusDriver.objects.get(Bus_id=Bus_id)
            bus_driver_serializer = serializers.NestedBusDriverSerializer(bus_driver_instance)
            Driver_name = bus_driver_serializer.data.get('Driver_id')['Driver_name']
            temp_dict['Driver_name'] = Driver_name
            response.append(temp_dict)
            temp_dict = {}

        return Response(response)
