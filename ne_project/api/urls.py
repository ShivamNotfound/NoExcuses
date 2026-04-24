from django.urls import path
from . import views
urlpatterns = [path("home/", views.Home.as_view(), name = "home"),
               path("select_equipment/", views.equipment_selection, name="select_equipment")]