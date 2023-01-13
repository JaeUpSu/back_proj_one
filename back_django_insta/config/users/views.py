from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from .models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError
from .serializers import MyInfoUserSerializer



# Create your views here.
def show_user(request):
    user_list = User.objects.order_by('date_joined')
    context = {"user_list":user_list}
    return render(request, 'users/user_list.html', context)

class Users(APIView):
    def post(self, request):
        password = request.data.get("password")
        serializer = MyInfoUserSerializer(data=request.data)
        
        try:
            validate_password(password)
        except:
            raise ParseError("Invalid password")
        
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:    
            return Response(serializer.errors)
    
        
class MyInfo(APIView):
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    
class Login(APIView):
    
    def post(self, request):
        user_id = request.data.get('username')
        user_pw = request.data.get('password')
    
        user = authenticate(request, username=user_id, password=user_pw)
        
        if user is not None:
            login(request, user=user)
            return Response({"message":"success"})    
        else:
            return Response({"message":"fail"})
    
class Logout(APIView):
    
    def post(self, request):
        logout(request)
        return Response({"message":"success"})
    
    
    
    
    
    
    
    
    
    
    
    
    
    