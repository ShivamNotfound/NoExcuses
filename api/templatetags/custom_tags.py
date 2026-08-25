from django import template
from api.models import Workout, MuscleGroup, SubMuscle
register = template.Library()

@register.simple_tag
def get_workout_counts(muscle, ids):
    submuscles = list(SubMuscle.objects.filter(muscle = muscle))
    return len(Workout.objects.filter(sub_muscle__in = submuscles, id__in = ids).distinct()) 

@register.simple_tag
def get_workout_counts_submuscle(ids, submuscle):
    return len(submuscle.workouts.filter(id__in = ids))

@register.simple_tag
def get_item(dictionary, key):
    return dictionary.get(key)