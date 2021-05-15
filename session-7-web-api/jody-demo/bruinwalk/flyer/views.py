from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

from .models import FlyerPerson

# Create your views here.

# List flyers
def index(request):
    # context = {
    #     "flyer_people": [],#["Jody", "Tim"],
    #     "favorite_number": 4
    # }
    flyer_people = FlyerPerson.objects.all()
    context = {
        "flyer_people": flyer_people
    }
    return render(request, 'index.html', context)

# Create flyer
def create_flyer(request):
    return render(request, 'create_flyer.html')

# Show flyer
def show_flyer(request, flyer_id):
    try:
        flyer_person = FlyerPerson.objects.get(id=flyer_id)
    except FlyerPerson.DoesNotExist:
        raise Http404("Person does not exist")
    context = {
        "flyer_person": flyer_person
    }
    return render(request, 'show_flyer.html', context)

def take_flyer(request, flyer_id):
    # Get flyer_person
    try:
        flyer_person = FlyerPerson.objects.get(id=flyer_id)
    except FlyerPerson.DoesNotExist:
        raise Http404("Person does not exist")
    # Increment counter
    flyer_person.flyers_given += 1
    flyer_person.save()
    # Redirect to /flyer/:id:
    return HttpResponseRedirect(reverse('flyer:show_flyer', args=(flyer_person.id,)))