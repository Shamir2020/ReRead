from django.shortcuts import render, redirect
from user_authintication.forms import RecentProduct
from django.http import HttpResponseRedirect
from .models import laptop
from django.contrib.auth.models import User
from user_authintication.models import Profile
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


@user_passes_test(lambda u: not u.is_authenticated, login_url='/')
def LoginPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, "User login successful")

            return redirect('/')
        else: 
            messages.error(request, "Invalid credentials !")

    return render(request, 'login.html', {})

@user_passes_test(lambda u: not u.is_authenticated, login_url='/')
def RegisterPage(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
    
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exist !')

        elif password1 != password2:
            messages.error(request, 'Passwords do not match !')
        else: 

            user = User.objects.create_user(username=username, first_name=name, email=email, password=password1)
            
            profile = Profile.objects.create(
                profileUser=user,
                name=name,
                email=email,
                phone=phone
            )

            return redirect('/')

    return render(request, 'register.html', {})


def Logout(request):

    print('Logout def triggered')

    if (request.user.is_authenticated):
    
        auth.logout(request)
        messages.info(request, "Logout successful")

        return redirect('/')
    
    return redirect('/')



def ProfilePage(request):


    return render(request, 'profile.html', {})





def send(req):
    return render(req,'user_auth/submit.html')
def details(request):
    if request.method == 'POST':
        frm= RecentProduct(request.POST)
        if frm.is_valid():
            print('Valid form')
            pas=frm.cleaned_data['password']
            rpas=frm.cleaned_data['re_pass']
            lap=frm.cleaned_data['laptop']
            rlap=frm.cleaned_data['re_laptop']
            eml=frm.cleaned_data['email']
            abt=frm.cleaned_data['about']
            txt=frm.cleaned_data['textarea']
            chk=frm.cleaned_data['checkbox']
            rm=frm.cleaned_data['ram']
            
            buy=laptop(password=pas,re_pass=rpas,laptop=lap,re_laptop=rlap,email=eml,about=abt,textarea=txt,checkbox=chk,ram=rm)
            buy.save()

            return HttpResponseRedirect('/auth/successfully')
        else:
            frm= RecentProduct(auto_id=True,label_suffix=' - ')
            print('GET Statement')
    frm = RecentProduct()
    return render(request, 'user_auth/recent.html',{'form' : frm})