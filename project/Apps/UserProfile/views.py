from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "UserProfile/index.html")