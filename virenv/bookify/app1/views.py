from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import user_profile
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def index(request):
    return render(request,'index.html')

# Create your views here.

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email):
                messages.info(request,"Email is taken")
                return redirect('signup')
            elif User.objects.filter(username=username):
                messages.info(request,"Username Taken")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save();

                user_login=auth.authenticate(username=username,password=password1)
                auth.login(request,user_login)


                user_model=User.objects.get(username=username)
                #creating profile object for the user
                new_profile=user_profile.objects.create(name=user_model,id_user=user_model.id)
                new_profile.save()
                
                return redirect('settings')

                
        

            
        else:
            messages.info(request,'Passwords not matching')
            return redirect('signup')

    else:
        return render(request,'signup.html')



def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return  redirect('index')

        else:
           messages.info(request,"Username and Password doesnot match")
           return redirect('signin')

    else:
     return render(request,'signin.html')
    
    

@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def settings(request):
    #userprofile=user_profile.objects.get(user=request.user)
    return render(request,'setting.html',)
