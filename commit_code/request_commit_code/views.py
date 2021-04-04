from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import CommitCodeRequest

def show_users_list(request):
    CommitCodeRequests = CommitCodeRequest.objects.all()
    CommitCodeRequests = CommitCodeRequests.values("users").distinct()
    return render(request, "request_commit_code/showUsersList.html", {"CommitCodeRequests":CommitCodeRequests})

def show_user_request_list(request,user_name:str):
    userDataList = CommitCodeRequest.objects.filter(users = user_name)
    return render(request, "request_commit_code/showUserRequestsList.html", {"userDataList":userDataList})
