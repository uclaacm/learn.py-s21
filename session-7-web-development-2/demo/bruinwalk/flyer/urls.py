from django.urls import path
from . import views

app_name = 'flyer'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:flyer_id>', views.flyer_stats, name="flyer_stats")
]