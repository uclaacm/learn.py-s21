from django.urls import path
from . import views

app_name="flyer"
urlpatterns = [
    path('', views.index),
    path('create', views.create_flyer, name="create_flyer"),
    path('<int:flyer_id>', views.show_flyer, name="show_flyer"),
    path('<int:flyer_id>/take_flyer', views.take_flyer, name="take_flyer"),
]