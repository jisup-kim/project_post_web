from django.shortcuts import render

def landing(request):
    return render(request, 'checklist/landing.html')

def lists(request):
    return render(request, 'checklist/lists.html')

# Create your views here.
