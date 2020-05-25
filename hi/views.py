from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from .models import Entry,Journal,AudioFile
from .forms import register,talknow
from .modules.speech import virtualassitant
# from django import templatetags
# from django import template

#import pyaudio
#from .modules.speech import audioprocess as audioRec

# Create your views here.
def home(request):
    form=""
    return render(request,'index.html',{"form":form});

def startlistener(request):
    ScreenText=virtualassitant.StartListenser();
    #form=talknow()
    form=""
    # # if request.method == 'POST':
    # #     form = talknow(response.POST)
    # #     if form.is_valid():
    # #         userinput = form.cleaned_data["Audio"]
    # #         #audio_file = request.FILES.get('audio')
    # #         # Register = Register(FirstName=FN)
    # #         TalkNow = talknow(Audio=userinput)
    # #         # Register.save()
    # #     return HTTPResponseRedirect("Processing")
    # # else:
    # #     form = talknow()
    return render(request,'index.html',{"form":form,"ScreenText":ScreenText});

def authenticate(request):
    user = authenticate(username='john', password='secret')
    if user is not None:
        result='authenticated'
    else:
        result='Not a valid user'
    return render(request,'login.html',"{'authenticate':result}")

def CreateUser(request):
    if request.method == 'POST':
        form = register(response.POST)
        if form.is_valid():
            FN=form.cleaned_data["FirstName"]
            LN=form.cleaned_data["LastName"]
            E=form.cleaned_data["Email"]
            P=form.cleaned_data["Password"]
            #Register = Register(FirstName=FN)
            #Register.save()
        return HTTPResponseRedirect("/%i" %R.id)
    else:
        form= register()
    return render(request,"register/register.html",{"form":form})
