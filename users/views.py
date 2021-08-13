from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from .serializers import UserSerializer
from django.contrib.auth.models import User, update_last_login
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework import status
from users import serializers
from .models import Users
from rest_framework.permissions import IsAuthenticated

class AddUser(APIView):
    def post(self,request):
        response = {}
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['message'] = "registeration successfull"
            response_status = status.HTTP_200_OK
        else:
            response['error'] = serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response,status=response_status)   

class GetAllUsers(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self,request):    
        try: 
            users =  Users.objects.all()
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        list_of_users = []
        user_object = {}
        
        for user in users:
            user_object['fullname'] =  user.fullname
            user_object['date_joined'] =  user.date_joined
            list_of_users.append(user_object)
            user_object = {}
        return Response(list_of_users,status=status.HTTP_200_OK)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
