from django.http import HttpResponse
from django.shortcuts import render
from .models import CommitCodeRequest

def show_request(request):
    commitCodes = CommitCodeRequest.objects.all()
    return render(request, "request_commit_code/showCommitCode.html", {"commitCodes":commitCodes})
