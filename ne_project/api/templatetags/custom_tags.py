from django import template
from api.models import Workout, MuscleGroup, SubMuscle
register = template.Library()

@register.simple_tag
def get_workout_counts(muscle, ids):
    return len(muscle.workouts.filter(id__in = ids))

@register.simple_tag
def get_workout_counts_submuscle(ids, submuscle):
    return len(submuscle.workouts.filter(id__in = ids))