from django.urls import path , include
from postal_post import views

urlpatterns = [
    path('', views.get_postal , name="get_postal" ),
]