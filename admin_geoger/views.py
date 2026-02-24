from django.shortcuts import render

def home(request):
    context={
      "message":"Welcome to the Admin Home Page"  
    }


    return render(request,'index.html',context)
