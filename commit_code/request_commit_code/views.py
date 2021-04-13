from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import CommitCodeRequest
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .private_method import private_login
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt
from .private_method import private_request_commit_code

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            
            if user:
                login(request, user)
                return show_users_list(request, user)
            else:
                return HttpResponse("密码错误！")
        else:
            return HttpResponse("Invalid login")
    
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "request_commit_code/login.html", {"form":login_form})

workLeader = set([
    "chaiyanglin","chenlvjie","xiangfenfen","liangyang","lihang3","lishihan","wangsihua",
    "柴阳林","陈吕杰","向芬芬","李昂阳","李航3","李世汉","王思华",
    "yhy",
    ]
)


@login_required(login_url='/request_commit_code/login/') 
@csrf_exempt
def show_user_request_list(request, user_name):
    userDataList = CommitCodeRequest.objects.filter(users = user_name)
    return render(request, "request_commit_code/showUserRequestsList.html", {"userDataList":userDataList})


@login_required(login_url='/request_commit_code/login/') 
@csrf_exempt
def show_users_list(request, user_name):
    if request.method == "GET":
        if str(user_name) in workLeader:
            CommitCodeRequests = CommitCodeRequest.objects.all()
            #CommitCodeRequests = CommitCodeRequests.values("users").distinct()
            return render(request, "request_commit_code/showUsersList.html", {"CommitCodeRequests":CommitCodeRequests})
        else:
            return show_user_request_list(request,user_name)

@login_required(login_url='/request_commit_code/login/') 
@csrf_exempt
def request_commit_code(request, user, code_path):
    if request.method == "POST":
        CommitCodeRequest.objects.create(user=user, column=code_path) 
        return HttpResponse("1")