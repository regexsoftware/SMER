from django.shortcuts import render

# Create your views here.
def get_multiple(request):
    return render(request,'multiple.html')