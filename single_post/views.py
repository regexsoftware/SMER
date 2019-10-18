from django.shortcuts import render

# Create your views here.
def get_single(request):
    return render(request,'single.html')