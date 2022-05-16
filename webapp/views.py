from pickle import TRUE
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from webapp.models import emplyoees
from webapp.serializers import employeesSerializer
# Create your views here.

class emplyoeeList(APIView):
    def get(self ,request):
        emplyoees1 = emplyoees.objects.all()
        serializer = employeesSerializer(emplyoees1,many =TRUE)
        return  Response(serializer.data)

    # def post(self):
    #     pass 