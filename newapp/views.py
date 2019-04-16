from _future_ import unicode_literals
from django.contrib.messages.views import successMessageMixin
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.reponse import Response
from django.http import JsonResponse
from .models import square
from .serializers import SquareSerializer
from rest_framework import status



@api_view(['GET'])
def getsquare(request,_number):
    call = Square.objects.filter(number=_number)
    print(list(call))
    if cal:
        serializer = SquareSerializer(cal,many=True)
        return Response(serializer.data)
        


# Create your views here.
