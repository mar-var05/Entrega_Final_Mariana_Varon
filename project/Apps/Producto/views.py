from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from . import models
# Create your views here.

def index  (request:HttpRequest) -> HttpResponse:
    return render(request,"Producto/index.html")