from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('about', views.AboutView.as_view(), name="about"),
    path('contact', views.ContactView.as_view(), name="contact"),
    path('media', views.MediaView.as_view(), name="media"),
]
