from django.urls import path , include
from user_profile import views

urlpatterns = [
    path('', views.get_user_profile , name="get_user_profile" ),
]