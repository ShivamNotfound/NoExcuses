from django.db import models

# Create your models here.

class Equipment(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name

class MuscleGroup(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name

class SubMuscle(models.Model):
    name = models.CharField(max_length = 30)
    muscle = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE, null= True)
    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length = 50)
    difficulty = models.PositiveSmallIntegerField()
    description = models.CharField(max_length = 500)
    equipment = models.ManyToManyField(Equipment, related_name = "workouts")
    muscle = models.ManyToManyField(MuscleGroup, related_name = "workouts")
    sub_muscle = models.ManyToManyField(SubMuscle, related_name = 'workouts')
    def __str__(self):
        return self.name


