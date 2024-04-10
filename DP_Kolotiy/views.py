from django.shortcuts import render

def github_gitlab(request):
    return render(request, 'github_gitlab.html')

def resume(request):
    return render(request, 'resume.html')