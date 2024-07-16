from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    est_dob = models.DateField()
    weight = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=1)
    medical_conditions = models.TextField()

class FeedingSchedule(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    food = models.CharField(max_length=100)
    amount = models.PositiveSmallIntegerField()
    frequency = models.CharField(max_length=100)

class ActivityLog(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=100)
    notes = models.TextField()
