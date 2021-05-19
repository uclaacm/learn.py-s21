from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def flyer_info(request, flyer_id):
  return render(request, 'flyer_info.html')