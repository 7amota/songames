from django.shortcuts import render, HttpResponse

def view(request):
    return render(request, 'base.html')
