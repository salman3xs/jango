from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from first_app import form
from first_app.models import Topic, Webpage, AccessRecord, User
from first_app.form import MyForm_Modal, UserProfileInfoForm

#login
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    user = User.objects.all()
    date_dict = {'ar': webpage_list, 'u': user}
    return render(request, 'first_app/index.html', context=date_dict)


def user(request):
    user = User.objects.all()
    user_dict = {'u': user}
    return render(request, 'first_app/user.html', context=user_dict)


def demo(request):
    return render(request, 'first_app/Dan/demo (1).html')


def myform(request):
    myform = form.MyForm()

    if request.method == 'POST':
        myform = form.MyForm(request.POST)

        if myform.is_valid():
            # Work
            print("Form Submitted")
            print(myform.cleaned_data['name'])

    return render(request, 'first_app/form_page.html', {'form': myform})


def myform2(request):

    registered = False

    if request.method == "POST":
        form = MyForm_Modal(request.POST)
        profile = UserProfileInfoForm(request.POST)

        if form.is_valid() and profile.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            pro = profile.save(commit=False)
            pro.user = user

            if 'profile_pic' in request.FILES:
                pro.profile_pic = request.FILES['profile_pics']
            
            pro.save()
            registered = True
            
        else:
            print(form.errors, profile.errors)

    else:
        form = MyForm_Modal()
        profile = UserProfileInfoForm()
    return render(request, 'first_app/form_page2.html', 
                  {'form': form, 
                   'profile_form': profile, 
                   'registered': registered})


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and falied")
            return HttpResponse("invalid Login details")
    
    else:
        return render(request, 'first_app/login.html')


@login_required    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app/index'))