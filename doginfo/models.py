from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=100, null=True)
    breed = models.CharField(max_length=100, null=True)
    est_dob = models.DateField(null=True)
    weight = models.PositiveSmallIntegerField(null=True)
    sex = models.CharField(max_length=1, null=True)
    medical_conditions = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name

class FeedingSchedule(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    food = models.CharField(max_length=100, null=True)
    amount = models.CharField(max_length=100, null=True)
    frequency = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.food

class ActivityLog(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=100, null=True)
    notes = models.TextField(null=True)

    def __str__(self) -> str:
        return self.activity
