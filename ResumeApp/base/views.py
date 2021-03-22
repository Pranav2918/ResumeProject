from django.shortcuts import render

def index(request):
    context = {'home' : 'active'}
    return render(request, 'base/index.html',context)

def contact(request):
    return render(request, 'base/contact.html')