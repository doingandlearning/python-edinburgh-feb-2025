from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import json

# Create your views here.

@api_view(["GET", "POST"])
@renderer_classes([JSONRenderer])
def drf_view(request):
    if request.method == "GET":
        return Response({"message": "Hello for DRF!"})
    else:
        return Response({"data": json.loads(request.body)})