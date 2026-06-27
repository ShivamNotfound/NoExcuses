from django.urls import path
from . import views
urlpatterns = [path("home/", views.Home.as_view(), name = "home"),
               path("select_equipment/", views.equipment_selection, name="select_equipment"),
               path("submuscles/<int:muscle_id>/<int:current>/", views.available_workouts_for_submuscle, name="available_workouts_submuscle"),
               path("submuscles/<int:muscle_id>/", views.available_workouts_for_submuscle, name="available_workouts_submuscle"),
               path("workout/<int:workout_id>/", views.workout_page, name = "workout_page"),
               path("login/", views.login, name="login"),
               path("register/", views.register, name="register"),
               path("logout/", views.logout, name="logout"),
               ]