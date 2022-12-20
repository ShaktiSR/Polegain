from django.contrib.auth import models
from django.contrib.auth.models import User, auth
from django.contrib import messages
#from django.core.checks import messages
from django.http import HttpResponse, response
from myapp.models import Contect, Poll
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .forms import CreatePollForm
from .models import Poll, ulimiter
from django.urls import path
#from django.shortcuts import render_to_response

##
#def hello(request):
    #return render(request, "myapp/pages/home.html")

#def index(request):
#    #return render(request, 'home.html')
#    return HttpResponse("<h1>This is landing page</h1>")

def daily_poll(request):
    #poll = Poll.objects.get(pk=id)
    #def vote(request):
    #context = {}
    #return render(request, 'poll/vote.html', context)
    poll=Poll.objects.all() #set of all movies

    context = {}
    return render(request=request, template_name="daily_poll.html", context={'poll':poll})

def vote(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'results.html', context)


def create_poll(request):
    if request.method == 'POST':
        uu=request.user.username
        quest=request.POST['question']
        op1=request.POST['option1']
        op2=request.POST['option2']
        op3=request.POST['option3']
        op4=request.POST['option4']
        #changing the limit for question
        gotmail=request.user.email
        obj=ulimiter.objects.get(uid=gotmail)
        if obj.ulimit<5:
            obj.ulimit += 1
            obj.save()
            user=Poll(loguser=uu,question=quest,option_one=op1,option_two=op2,option_three=op3,option_four=op4)
            user.save()
            return redirect('home')    
        else:
            return HttpResponse('You have reached your limit of 5 for creating poll.')
            #return render(request, 'home.html', {'alert_flag': True})
            #return render_to_response('user_profile.html', message='Save complete')
    return render(request, 'create_poll.html')
    #return HttpResponse("This is about page")



def home(request):
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return redirect('home.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check if user has entered correct pwd
        user = authenticate(username=username, password=password)
        #print("HHHHHHHHHHHHHHHHOOOOOOOOOOOME",user)
        if user is not None:
            login(request,user)
            return redirect("home")
            # A backend authenticated the credentials
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
            


    return render(request,'login.html')


def regist(request):
    #pass1=request.POST.get('password')
    #pass2=request.POST.get('cpassword')
    if request.method=="POST":
        mail=request.POST['gmail']
        uname=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['cpassword']
        
        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username taken")
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"email alredy exists!")
            else:
                ul=ulimiter(uid=mail,ulimit=0)
                ul.save()
                user=User.objects.create_user(username=uname,password=pass1,email=mail)
                user.save()
                messages.info(request,"user created")
                return redirect("login")
        else:
            messages.info(request,"Password not matching")
    return render(request,'regist.html')

def user_profile(request):
    #cu=request.user
    #gotmail=request.user.email
    #ulimiter.uid=gotmail
    #print("________+_+_+_+_+_+_+_+_+++_= ",gotmail)
    #obj=ulimiter.objects.get(uid=gotmail)
    #obj.ulimit += 1
    #print("________+_+_+_+_+_+_+_+_+++_= ",obj.ulimit)
    #obj.save()
    #print("________+_+_+_+_+_+_+_+_+++_= ",gotmail)
    ulim=ulimiter.objects.all()
    poll=Poll.objects.all()
    context = {}
    return render(request=request, template_name="user_profile.html", context={'poll':poll,'ulim':ulim})


# Create your views here.
