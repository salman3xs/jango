from first_app import views
from django.urls import path

urlpatterns = [
    path('index/',views.index),
    path('demo/',views.demo),
    path('user/',views.user),
    path('form/',views.myform)
]