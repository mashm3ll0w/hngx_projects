from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Person
# Create your views here.

def index(request):
  return JsonResponse({"greeting": "How are you doing?"}, safe=False)
