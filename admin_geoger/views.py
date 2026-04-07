from django.shortcuts import render
from rest_framework import viewsets
from .models import direccion
from .serializers import DireccionSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = direccion.objects.all()
    serializer_class = DireccionSerializer

def home(request):
    context={
      "message":"Welcome to the Admin Home Page"  
    }
    
    return render(request,'index.html',context)


