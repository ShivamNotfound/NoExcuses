from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
# Create your views here.
from django.views import generic
from .models import Equipment, MuscleGroup, Workout, SubMuscle
from django.db.models import Count



class Home(generic.ListView):
    model = MuscleGroup
    queryset = MuscleGroup.objects.prefetch_related()
    def get_template_names(self):
        return "api/home.html"
    def get_context_object_name(self, object_list):
        self.request.session = list(Workout.objects.all().values_list("id", flat=True))
        return "muscles"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workouts"] = Workout.objects.all()
        return context
    
@csrf_protect
def equipment_selection(request):
    if request.method == 'POST':
        ids = list(request.POST.keys())[1:]
        selected_equipments = Equipment.objects.filter(id__in = ids)
        workouts = Workout.objects.filter(equipment__in = selected_equipments)
        print(workouts)
        request.session['workout_ids'] = list(workouts.values_list("id", flat=True))
        return redirect("available_workouts")
    equipments = Equipment.objects.prefetch_related()
    context = {"equipments": equipments}
    return render(request, 'api/select_equipment.html', context)

def available_workouts(request):
    ids = request.session.get("workout_ids")
    muscles = MuscleGroup.objects.prefetch_related()
    context = {"muscles":muscles,"ids":ids}
    return render(request,"api/available_workouts.html", context)

def available_workouts_for_submuscle(request, muscle_id, current = -1):
    
    ids = request.session.get("workout_ids")
    submuscles = SubMuscle.objects.filter(muscle__id = muscle_id)
    workouts = submuscles[0].workouts.all() if current == -1 else SubMuscle.objects.get(id = current).workouts.all()
    context = {"ids":ids, "muscle_id":muscle_id, "submuscles":submuscles, "workouts_selected":workouts}
    return render(request, "api/available_workouts_submuscle.html", context)

def workout_page(request, workout_id):
    workout = Workout.objects.get(id = workout_id)

    context = {"workout":workout}
    return render(request, "api/workout.html", context)