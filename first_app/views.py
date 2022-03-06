from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User
# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    user = User.objects.all()
    date_dict = {'ar': webpage_list,'u':user}
    return render(request, 'first_app/index.html',context=date_dict)

def user(request):
    user = User.objects.all()
    user_dict = {'u':user}
    return render(request, 'first_app/user.html',context=user_dict)

def demo(request):
    return render(request, 'first_app/Dan/demo (1).html')   