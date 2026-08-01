from django.contrib import admin
from .models import Equipment, Workout, MuscleGroup, SubMuscle, Steps, WorkoutMedia
# Register your models here.

admin.site.register(Equipment)
admin.site.register(Workout)
admin.site.register(MuscleGroup)
admin.site.register(SubMuscle)
admin.site.register(Steps)
admin.site.register(WorkoutMedia)