from django.urls import path
from . import views

app_name = 'flyer'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:flyer_id>', views.flyer_info, name="flyer_info"),
    path('<int:flyer_id>/take_flyer', views.take_flyer, name="take_flyer")
]