from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
# Create your views here.
from django.views import generic
from .models import Equipment, MuscleGroup, Workout, SubMuscle
from django.contrib.auth.models import User

class Home(generic.ListView): 
    model = MuscleGroup
    queryset = MuscleGroup.objects.prefetch_related()
    def get_template_names(self):
        return "api/home.html"
    def get_context_object_name(self, object_list):
        return "muscles"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ids = self.request.session.get("equipment_ids", -1)
        if ids==-1:
            workouts = Workout.objects.all()
            context["text"] = "Add equipments"
        else:
            workouts = Workout.objects.filter(equipment__id__in = ids).distinct()
            context["text"] = "Change equipments"
        context["workouts"] = workouts
        context["ids"] = workouts.values_list("id", flat=True)
        return context
    
@csrf_protect
def equipment_selection(request):
    if request.method == 'POST':
        ids = list(request.POST.keys())[1:] # Remove blurbar and fix this.
        request.session['equipment_ids'] = ids
        selected_equipments = Equipment.objects.filter(id__in = ids)
        workouts = Workout.objects.filter(equipment__in = selected_equipments)
        return redirect("home")
    equipments = Equipment.objects.prefetch_related()
    context = {"equipments": equipments}
    return render(request, 'api/select_equipment.html', context)

@csrf_protect
def available_workouts_for_submuscle(request, muscle_id, current = 0):
    ids = request.session.get("equipment_ids", -1)
    if(ids == -1):
        ids = Workout.objects.all().values_list("id", flat = True)
    submuscles = SubMuscle.objects.filter(muscle__id = muscle_id)
    if current!=0:
        submuscle = SubMuscle.objects.get(id = current)
        active = submuscle.id
        workouts = Workout.objects.filter(equipment__id__in = ids, sub_muscle = submuscle).distinct()
    else:
        workouts = Workout.objects.filter(equipment__id__in = ids, sub_muscle = submuscles[0]).distinct()
        active = submuscles[0].id
    ids = Workout.objects.filter(equipment__id__in = ids).values_list("id", flat = True)
    context = {"ids":ids, "muscle_id":muscle_id, "submuscles":submuscles, "workouts_selected":workouts.order_by("-hypertrophy_score"), "active":active, "current":current}
    context["select"] = 0
    context["diff"] = 0
    if request.method == 'POST':
        options = ["-hypertrophy_score", "-strength_score", "-endurance_score"]
        option = request.POST.get("option")
        difficulty = request.POST.get("difficulty")
        diff = 0
        workouts = workouts.order_by(options[int(option)])
        if difficulty == "eth":
            workouts = workouts.order_by("difficulty",options[int(option)])
            diff = 1
        elif difficulty == "hte":
            workouts = workouts.order_by("-difficulty", options[int(option)])
            diff = 2
        context["workouts_selected"] = workouts
        context["select"] = option
        context["diff"] = diff
    return render(request, "api/available_workouts_submuscle.html", context)

def workout_page(request, workout_id):
    workout = Workout.objects.get(id = workout_id)
    context = {"workout":workout}
    return render(request, "api/workout.html", context)

@csrf_protect
def login(request):
    if request.method == 'POST':
        mail = request.POST.get('email')
        password = request.POST.get('password')

    return render(request, "api/login.html")

@csrf_protect
def register(request):
    if request.method == 'POST':
        mail = request.POST.get('email')
        password = request.POST.get('password')
        
    return render(request, "api/register.html")