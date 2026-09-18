from django import template
from api.models import Workout, MuscleGroup, SubMuscle
register = template.Library()

@register.simple_tag
def get_workout_counts(muscle, workouts, submuscles):
    submuscles = list(submuscles.filter(muscle = muscle))
    return len(workouts.filter(sub_muscle__in = submuscles).distinct()) 

@register.simple_tag
def get_workout_counts_submuscle(ids, submuscle):
    return len(submuscle.workouts.filter(id__in = ids))

@register.simple_tag
def get_item(dictionary, key):
    return dictionary.get(key)