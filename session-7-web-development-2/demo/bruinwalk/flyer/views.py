from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from .models import FlyerPerson
# Create your views here.

def index(request):
  flyer_people = FlyerPerson.objects.all()
  context = {
    'flyer_people': flyer_people
  }
  return render(request, "index.html", context)


def flyer_stats(request, flyer_id):
  try:
    person = FlyerPerson.objects.get(id=flyer_id)
  except(FlyerPerson.DoesNotExist):
    raise Http404("Person does not exist")
  context = {
    'person': person
  }
  return render(request, "flyer_stats.html", context)

def take_flyer(request, flyer_id):
  try:
    person = FlyerPerson.objects.get(id=flyer_id)
  except(FlyerPerson.DoesNotExist):
    raise Http404("Person does not exist")
  person.flyers_given += 1
  person.save()
  return HttpResponseRedirect(reverse('flyer:flyer_stats', args=(person.id,)))