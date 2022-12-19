from django.shortcuts import render

def index(request):
    context={
        "title":"Bienvenue à AKEA-TECH",
    }
    return render(request, "site/index.html", context)