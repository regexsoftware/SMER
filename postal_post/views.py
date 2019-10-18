from django.shortcuts import render

# Create your views here.
def get_postal(request):
    return render(request,'postal.html')