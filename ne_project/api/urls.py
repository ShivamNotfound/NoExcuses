from django.urls import path
from . import views
urlpatterns = [path("home/", views.Home.as_view(), name = "home"),
               path("select_equipment/", views.equipment_selection, name="select_equipment"),
               path("muscles/", views.available_workouts, name = "available_workouts"),
               path("submuscles/<int:muscle_id>", views.available_workouts_for_submuscle, name="available_workouts_submuscle")]