# learn<span>.</span>py Session 7: Web Developement 2 <!-- omit in toc -->

**Date**: May 19, 2021

**Location**: Zoom

**Teachers**: [Timothy Rediehs](https://github.com/timthetic)

## Resources <!-- omit in toc -->

- [Slides](http://links.uclaacm.com/learnpy21-s5-slides)
- [ACM Membership Attendance Portal](https://members.uclaacm.com/login)

## What we'll be learning today <!-- omit in toc -->
- [A Quick Intro to Databases](#a-quick-intro-to-databases)
  - [About Models](#about-models)
  - [Migrations](#migrations)
- [Demo: Databases](#demo-databases)

## A Quick Intro to Databases
We use databases to store information our app needs persistently. This means that restarting the server will not cause the data to be lost. Django comes with sqlite, one of many databases, out of the box along with an easy to use interface for it. You can think of sqlite as a big collection of tables (kind of like and Excel sheet, but way better).

### About Models
Django provides us with a special `models.Model` object that helps us interact with our database. We can create new tables by making a new subclass of `models.Model` and modify the structure of those tables by modifying our subclasses. Another benefit of models is that we don't have to know any SQL! Instead of saying `SELECT * FROM fruit`, we could say something like `Fruit.objects.all()` and get our response in a convenient Python list.

### Migrations
There are two important commands for when we create or modify our database models:
```py
python manage.py makemigrations flyer
python manage.py migrate
```
These commands will look at your models and create the appropriate database migrations to synchronize your database with your models (the second command executes those migrations). These migrations allow you to keep track of changes to your database as well as safely make changes without having to worry too much about losing all your data. This is a big deal for applications that are being used in production.

## Demo: Databases
The first thing we'll do is create a database model in flyer/models.py. Edit that file so it looks like this:

```py
from django.db import models

# Create your models here.
class FlyerPerson(models.Model):
    name = models.CharField(max_length=100)
    pitch = models.CharField(max_length=300)
    flyers_given = models.IntegerField()
```

We inherit from the `models.Model` class because our `FlyerPerson` needs to be a database object with all of the functionality to interact with the database. We can add any fields we want and give them one of several types. Here is a list of some useful ones:

* Boolean: `models.BooleanField()`
* Date/time: `models.DateTimeField()`
* Float: `models.FloatField()`
* Number: `models.IntegerField()`
* Text: `models.CharField(max_length=N)` or `models.TextField()`

Django comes with some useful admin tools that we can use to see our database tables, but we need to create a superuser to use them. We can do this with two commands.

```
python manage.py migrate
python manage.py createsuperuser
```

`python manage.py migrate` will create some necessary tables for our superuser. Then `python manage.py createsuperuser` will create our superuser. Follow the prompts to create the superuser.

Next, try running the server with `python manage.py runserver` and navigating to localhost:8000/admin. Enter the username and password of your superuser, then you should see a screen like this: 

<img src="./assets/admin_page.png" width=500>

We should be able to see our tables here, but oh no! Our tables are nowhere to be found. This is because we did not create and run the migration for our new table (we only ran the migrations for some of Django's bookkeeping tables). Let's do that now.

```
python manage.py makemigrations flyer
python manage.py migrate
```

These commands will create the migrations for our models in our flyer app, then run them. Now, if we start our server with `python manage.py runserver` again, `localhost:8000/admin` should show our table, right? Not yet. It turns our that our admin page doesn't know our model exists. We have to tell it by modifying flyer/admin.py to look like the following:

```py
from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.FlyerPerson)
```

Now our model should show up:
<img width=500 src="./assets/admin_model.png">

If you click on the add button with a green plus, it should bring you to a page that let's you create new Flyer People in the database. Add two Flyer People. You should see them in the Flyer Persons section of the admin page.

<img width=500 src="./assets/admin_objects.png">

Next, we want to rewrite our views and templates to use our new models. First, let's modify flyer/views.py. We'll need to import our model using `from .models import FlyerPerson`. Then, we can rewrite the `index` function as follows:

```py
def index(request):
  flyer_people = FlyerPerson.objects.all()
  context = {
    'flyer_people': flyer_people
  }
  return render(request, "index.html", context)
```
It's very similar to what we had before, accept we fill our flyer_people with all the objects in our database using `FlyerPerson.objects.all()`. Let's try running our server and see what happens.

<img width=500 src="./assets/incomplete_template.png"/>

Oh no, what on earth is `FlyerPerson object (1)`? Our flyer people used to be just strings, if we want to display their names, we'll have to change `flyer/templates/index.html` as show below:

```html
{% for person in flyer_people %}
<li><a href="{% url 'flyer:flyer_stats' person.id  %}">{{ person.name }}</a>: {{ person.pitch }}</li>
{% endfor %}
```

This should look like the following now:

<img width=500 src="./assets/complete_template.png">

Next, we can modify our `flyer_stats` view in a similar way. In `flyer/views.py` modify the `flyer_stats` function to the following

```py
def flyer_stats(request, flyer_id):
  try:
    person = FlyerPerson.objects.get(id=flyer_id)
  except(FlyerPerson.DoesNotExist):
    raise Http404("Person does not exist")
  context = {
    person: person
  }
  return render(request, "flyer_stats.html", context)
```
This is similar to before, but we only get a single Flyer Person with a specific id using `FlyerPerson.objects.get(id=flyer_id)`. Next, we'll need to modify `flyer/templates/flyer_stats` to use our new model:

```html
<h1>Flyer Person Stats</h1>
<p>Information about flyer person</p>

<h2>{{ person.name }}</h2>
<p>{{ person.pitch }}</p>
<p>Flyers given: {{ person.flyers_given }}</p>
```

Perfect. Next, we want to add a button on the flyer_stats page that lets you take a flyer (increments the flyers_given counter by one). To do this, we can just add an html form to the flyer_stats template and a take_flyer view to our flyer/views.py file.

> Note: while our new take_flyer function in in the `views.py` file, it's not really a view as much as a block of code that we can ask to execute from our html form. This will become clearer as the demo progresses.

First, we can add the basics of an html form to the end of the body of `flyer/templates/flyer_stats.html`:

```html
<form>
    {% csrf_token %}
    <input type="submit" value="Vote">
</form>
```

This just adds a button to the page that is part of a form. It does nothing else for now. `{% csrf_token %}` is a built in function that helps us prevent [cross-site request forgeries](https://owasp.org/www-community/attacks/csrf). Next, let's build `take_flyer()` in `flyer/views.py`.

```py
from django.http.response import Http404, HttpResponseRedirect
from django.urls.base import reverse
def take_flyer(request, flyer_id):
  try:
    person = FlyerPerson.objects.get(id=flyer_id)
  except(FlyerPerson.DoesNotExist):
    raise Http404("Person does not exist")
  person.flyers_given += 1
  person.save()
  return HttpResponseRedirect(reverse('flyer:flyer_stats', args=(person.id,)))
```

This should get the correct Flyer Person, then try to increment their number of flyers given. The last line will redirect the user to our flyer_stats page using `person.id` (/flyers/:id). Remember that we named that url "flyer_stats" using the name parameter and the `app_name` in `urls.py` is "flyer", hence "flyer:flyer_stats".

We also need to add an entry in `urls.py` for this new view:

```py
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:flyer_id>', views.flyer_stats, name="flyer_stats"),
    path('<int:flyer_id>/take_flyer', views.take_flyer, name="take_flyer") # This line is new
]
```

Finally, we can add an "action" to our html form to submit a request to our new endpoint when the button is clicked. We do that as follows:

```py
<form action="{% url 'flyer:take_flyer' person.id %}" method="post">
    {% csrf_token %}
    <input type="submit" value="Vote">
</form>
```

This will send a POST request to our new endpoint which will run our code to increment the counter in our model. With that, we've finished our flyer feature.
