from django.shortcuts import render

# Create your views here.
def get_user_profile(request):
    return render(request,'profile.html')