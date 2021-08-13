from django.urls import path

from . import views

urlpatterns = [
    path('routes', views.AllRoutes.as_view()),
    path('locations', views.ViewLocations.as_view()),
    path('addlocation', views.AddLocation.as_view()),
    path('buses', views.ViewBuses.as_view())
]