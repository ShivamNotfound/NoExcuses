from django.contrib import admin
from .models import Equipment, Workout, MuscleGroup, SubMuscle
# Register your models here.

admin.site.register(Equipment)
admin.site.register(Workout)
admin.site.register(MuscleGroup)
admin.site.register(SubMuscle)