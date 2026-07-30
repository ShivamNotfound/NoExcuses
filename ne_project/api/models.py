from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
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
    class DifficultyChoices(models.TextChoices):
        EASY = 'easy', 'easy'
        MEDIUM = 'medium', 'medium'
        HARD = 'hard', 'hard'
    class TypeChoices(models.TextChoices):
        ISOLATED = 'isolated','isolated'
        COMPOUND = 'compound', 'compound'
    name = models.CharField(max_length = 50)
    difficulty = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(2)]
    )
    description = models.TextField(max_length = 500)
    equipment = models.ManyToManyField(Equipment, related_name = "workouts")
    sub_muscle = models.ManyToManyField(SubMuscle, related_name = 'workouts')
    type = models.CharField(choices = TypeChoices, max_length = 20)
    strength_score = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(10)]
    )
    hypertrophy_score = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(10)]
    )
    endurance_score = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.name

class Steps(models.Model):
    workout = models.ForeignKey(Workout, on_delete = models.CASCADE)
    step_number = models.PositiveSmallIntegerField()
    instruction = models.TextField(max_length = 200)
    image_url = models.CharField(max_length = 30)
class WorkoutMedia(models.Model):
    class TypeChoices(models.TextChoices):
        IMAGE = 'image', 'image'
        VIDEO = 'video', 'video'
    workout = models.ForeignKey(Workout, on_delete= models.CASCADE)
    url = models.CharField(max_length = 30)
    type = models.CharField(choices = TypeChoices, max_length = 20)
    category = models.CharField(max_length = 30)
    caption = models.CharField(max_length = 50)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    equipment_ids = models.JSONField(default=list)