# learn<span>.</span>py Session 6: Web Development with Django

**Date**: May 12, 2021

**Location**: Zoom

**Teachers**: [Alex Xia](https://github.com/khxia), [Eric Yang](https://github.com/eric8yang)

## Resources

- [Slides](https://docs.google.com/presentation/d/1s6wGAEY1QgEpCxD-nfCVepwHw3ZvgRHc80DslN32Sn8/edit?usp=sharing)
- [ACM Membership Attendance Portal](https://members.uclaacm.com/login)

## What we'll be learning today
- [Intro to Web Development](#intro-to-web-development)
- [HTML](#html)
- [CSS](#css)
- [Django](#django)


> Note: This workshop series is designed with the assumption that attendees have taken CS31/PIC10A, or any of its equivalents. While we will go through the basics of Python, we do not explain all the details and fundamentals. Rather, we are showing how to what you have previously done, but within Python.

## Intro to Web Development

## HTML

## CSS

## Django
Django is a web framework for Python. What this means is that it essentially allows you to create a web application with the combination of HTML/CSS and Python files. One reason we choose to use Django is that it handles displaying more than 1 page of an website. Specifically, Django also serves as the "server" for you to try and send requests to. Since Django is all we need to begin turning our HTML/CSS into a working web application, we treat it as a "one-stop shop" for everything we need.

### Set-up
In order to begin working with Django, you first have to install Django using Terminal and running either `pip3 install django` (Mac) or `pip install django` (Windows). To check that the installation happened properly, you can run `python3 -m django --version` (Mac) or `python -m django --version` (Windows) to see if there is indeed an updated version of Django installed.

### Creating/running a project
To create and run a Django project, we will once again be running some lines in terminal. In order to create a project called "mysite", you can run the line `django-admin startproject mysite`. After the installation, you can navigate into the project and run `python3 manage.py runserver` (Mac) or `python manage.py runserver` (Windows). If everything worked properly, you should end up with a few messages about your server starting up. One of the lines you will see is `Starting development server at http://127.0.0.1:8000/`. While this may look confusing at first, you can break down this URL into 2 parts. First, the 127.0.0.1 part is a IP address that refers to your localhost. This may be familiar if you've had experience working with other development servers. If not, all this means is that the server you are developing on is hosted on your local computer. The second part is 8000, which just explains which port the server is running on. To see your current page, just direct your browser to [http://localhost:8000/](http://localhost:8000/). Since none of your files are in the project yet, you should just see a default Django page.

### Displaying your own files
In your project, you will see another folder with the same name as your project (I know, confusing). To differentiate between the two, I'll refer to the outermost folder as 'the project' and the inner folder as the `valorant` directory (in your case substitue "valorant" with whatever you named your project). Let's start by creating a folder in the project. We're going to name this `templates` and it'll hold all of our HTML files. Add the HTML files that you created for the previous half of the workshop to this folder and name it `index.html`.

We know that pages are displayed when servers return files for a given request. To handle requests that come in, create a file named `views.py` in the `valorant` directory
```py
from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')
```

In this code we are using the render function from the Django module to render index.html whenever the `home_page` function is called. However, you'll notice that the exact path to `index.html ` is not defined. The reason for this is that we can actually tell Django where to find your files. 

Within the `settings.py` file, you'll see a `TEMPLATES` variable with a `DIRS` key. Change that line to the following:
```py
'DIRS': [os.path.join(BASE_DIR,'templates')],
```
You'll see here that we're making use of something called `os`. os is actually a module that helps simplify the definition of file locations. To use it though, we'll need to add the line
```py
import os
```
to the top of our `settings.py` file. Feel free to explore os more on your own, but just know that what this function does is join the location specified by `BASE_DIR` (a variable a bit higher up in `settings.py`) with templates. `BASE_DIR` actually holds the path to your project, and `templates` is the name of your folder where HTML files are found. Thus, the combination of the two gives the entire path to your templates folder. 

Next up, we have to handle the process from the URL being requested and the expected files being rendered. We've defined the function `home_page` to render the `index.html` file, but we haven't yet defined when the `home_page` function will be called. In `urls.py`, you'll see that `urlpatterns` currently has 1 path defined. Let's create another one by adding `path('', views.home_page),` right below `path('admin/', admin.site.urls),` in the list. Doing so specifies that in the case that there is no extension after the URL (in order words, just `localhost:8000`), we are going to call the `home_page` function from views. However, we also need to make sure to import `views.py` so we can use its functions. To do this, we simply add the line `from . import views` to the top of the file. All this means is that we are importing the view module from . (which refers to the current directory).

Now if you try reloading your `localhost:8000` page, you should see the `index.html` file that you defined previously. However, one thing you may notice is that all of your styling is not there anymore. Similar to the situation we had with `index.html`, we need to tell Django where to look for the CSS files.

Let's first create the directory for our CSS files. We'll being by creating a folder named `static` in the project, and this folder will serve the purpose of holding all of our static files like CSS, images, etc. Within that `static` folder, we're going to create a new folder named `css`, which as the name suggests, will contain only CSS files. Copy the CSS file you made for the first half of the workshop here and rename it to `style.css`.

Moving to the `settings.py` file again, we're going to add a new tuple with the path to our `static` folder to the bottom of the file. It should look something like:
```py
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```
Now that we've got the static file set up, we also need to change some of the linking in the HTML files. You can edit your `index.html` file's link tag to:
```HTML
<link rel="stylesheet" href="static/css/style.css"/>
```
After completing these steps, your page should now show up with styling!

### Handling multiple pages
In order to serve multiple pages based on the URL, you follow similar steps that we went over for the `index.html` page. For example, let's say I created a file named `jett.html`. I would first make a function in `views.py` that looks something like:
```py
def jett(request):
    return render(request, 'jett.html')
```
This function will render the `jett.html` page when called. Then in `urls.py`, I can add the line
```py
path('jett/', views.jett),
```
to call the jett function when /jett/ is appended to the URL of `localhost:8000`. We can continue doing this for further files we want to display.
