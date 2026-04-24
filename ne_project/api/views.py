from django.shortcuts import render
# Create your views here.
from django.views import generic
from .models import Equipment, MuscleGroup, Workout



class Home(generic.ListView):
    model = MuscleGroup
    queryset = MuscleGroup.objects.prefetch_related()
    def get_template_names(self):
        return "api/home.html"
    def get_context_object_name(self, object_list):
        return "muscles"
    
def equipment_selection(request):

    if request.method == 'GET':
        ids = list(request.GET.keys())
        selected_equipments = Equipment.objects.filter(id__in = ids)
        workouts = Workout.objects.filter(equipment__in = selected_equipments)
        print(workouts)

    equipments = Equipment.objects.prefetch_related()

    context = {"equipments": equipments}
    return render(request, 'api/select_equipment.html', context)




