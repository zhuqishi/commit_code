from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import CommitCodeRequest
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            
            if user:
                login(request, user)
                return show_users_list(request)
            else:
                return HttpResponse("Sorry, your username or password is not right.")
        else:
            return HttpResponse("Invalid login")
    
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "request_commit_code/login.html", {"form":login_form})


def show_users_list(request):
    CommitCodeRequests = CommitCodeRequest.objects.all()
    CommitCodeRequests = CommitCodeRequests.values("users").distinct()
    return render(request, "request_commit_code/showUsersList.html", {"CommitCodeRequests":CommitCodeRequests})

def show_user_request_list(request,user_name:str):
    userDataList = CommitCodeRequest.objects.filter(users = user_name)
    return render(request, "request_commit_code/showUserRequestsList.html", {"userDataList":userDataList})
