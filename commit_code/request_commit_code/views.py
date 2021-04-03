from django.http import HttpResponse
from django.shortcuts import render
from .models import CommitCodeRequest

def show_request(request):
    commitCodes = CommitCodeRequest.objects.all()
    return render(request, "request_commit_code/showCommitCode.html", {"commitCodes":commitCodes})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    return HttpResponse("Hello, world. You're at the polls index.")