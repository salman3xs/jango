from django.shortcuts import render
from django.http import HttpResponse
from first_app import form
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

def myform(request):
    myform = form.MyForm()
    
    if request.method == 'POST':
        myform = form.MyForm(request.POST)
        
        if myform.is_valid():
            #Work
            print("Form Submitted")
            print(myform.cleaned_data['name'])
        
    return render(request, 'first_app/form_page.html',{'form':myform})