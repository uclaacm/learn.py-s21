from django.shortcuts import render

# Create your views here.

def index(request):
  context = {
    'name': 'narnar',
    'pitch': 'come haccc with us',
    'age': 18,
    'flyer_people': ['tim', 'jody', 'andre']
  }
  return render(request, "index.html", context)


def flyer_stats(request, flyer_id):
  context = {
    'name': 'Jody',
    'pitch': 'Do you want to save the bees?',
    'flyers_given': 0
  }
  return render(request, "flyer_stats.html", context)

