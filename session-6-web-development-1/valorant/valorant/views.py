from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')

def jett(request):
    return render(request, 'jett.html')

def jettWithNum(request, num):
    return render(request, 'jett' + str(num) '.html')