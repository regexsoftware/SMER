from django.urls import path , include
from single_post import views

urlpatterns = [
    path('', views.get_single , name="get_single" ),
]