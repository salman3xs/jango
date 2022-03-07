from first_app import views
from django.urls import path

app_name = 'first_app'

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('demo/',views.demo,name = 'demo'),
    path('user/',views.user,name = 'user'),
    path('form/',views.myform,name = 'myform'),
    path('form2/',views.myform2,name = 'myform2'),
    path('login/',views.login_view,name='login')
]