from django.shortcuts import render
from django.http import HttpResponse
from .models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MyInfoUserSerializer

# Create your views here.
def show_user(request):
    user_list = User.objects.order_by('date_joined')
    context = {"user_list":user_list}
    return render(request, 'users/user_list.html', context)

class MyInfo(APIView):
    def get(selfl, request):
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
    