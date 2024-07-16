from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Dog, FeedingSchedule, ActivityLog


def view_dogs(request):
    dogs = Dog.objects.all()
    jsondata = serializers.serialize('json', dogs)
    return HttpResponse(jsondata, content_type='application/json')

def view_dog_by_id(request, id):
    dog = Dog.objects.get(pk=id)
    jsondata = serializers.serialize('json', [dog])
    return HttpResponse(jsondata, content_type='application/json')

def view_dog_by_name(request, dog_name):
    dog = Dog.objects.filter(name=dog_name)
    jsondata = serializers.serialize('json', dog)
    return HttpResponse(jsondata, content_type='application/json')

def create_dog(request):
    dog = Dog()
    dog.name = request.POST['name']
    dog.breed = request.POST['breed']
    dog.est_dob = request.POST['est_dob']
    dog.weight = request.POST['weight']
    dog.sex = request.POST['sex']
    dog.medical_conditions = request.POST['medical_conditions']
    dog.save()

def update_dog(request, id):
    dog = Dog.objects.get(pk=id)
    dog.name = request.POST['name']
    dog.breed = request.POST['breed']
    dog.est_dob = request.POST['est_dob']
    dog.weight = request.POST['weight']
    dog.sex = request.POST['sex']
    dog.medical_conditions = request.POST['medical_conditions']
    dog.save()

def delete_dog(request, id):
    dog = Dog.objects.get(pk=id)
    dog.delete()

def view_feeding_schedule(request):
    feeding_schedule = FeedingSchedule.objects.all()
    jsondata = serializers.serialize('json', feeding_schedule)
    return HttpResponse(jsondata, content_type='application/json')

def view_feeding_schedule_for_dog(request, dog_id):
    feeding_schedule = FeedingSchedule.objects.filter(dog=dog_id).latest('id')
    jsondata = serializers.serialize('json', feeding_schedule)
    return HttpResponse(jsondata, content_type='application/json')

def create_feeding_schedule(request):
    feeding_schedule = FeedingSchedule()
    feeding_schedule.dog = Dog.objects.get(pk=request.POST['dog_id'])
    feeding_schedule.food = request.POST['food']
    feeding_schedule.amount = request.POST['amount']
    feeding_schedule.frequency = request.POST['frequency']
    feeding_schedule.save()

def update_feeding_schedule(request, id):
    feeding_schedule = FeedingSchedule.objects.get(pk=id)
    feeding_schedule.dog = Dog.objects.get(pk=request.POST['dog_id'])
    feeding_schedule.food = request.POST['food']
    feeding_schedule.amount = request.POST['amount']
    feeding_schedule.frequency = request.POST['frequency']
    feeding_schedule.save()

def delete_feeding_schedule(request, id):
    feeding_schedule = FeedingSchedule.objects.get(pk=id)
    feeding_schedule.delete()

def view_activity_log(request):
    activity_log = ActivityLog.objects.all()
    jsondata = serializers.serialize('json', activity_log)
    return HttpResponse(jsondata, content_type='application/json')

def view_activity_log_for_dog(request, dog_id):
    activity_log = ActivityLog.objects.filter(dog=dog_id).order_by('-date')
    jsondata = serializers.serialize('json', activity_log)
    return HttpResponse(jsondata, content_type='application/json')

def create_activity_log(request):
    activity_log = ActivityLog()
    activity_log.dog = Dog.objects.get(pk=request.POST['dog_id'])
    activity_log.activity = request.POST['activity']
    activity_log.notes = request.POST['notes']
    activity_log.save()

def update_activity_log(request, id):
    activity_log = ActivityLog.objects.get(pk=id)
    activity_log.dog = Dog.objects.get(pk=request.POST['dog_id'])
    activity_log.activity = request.POST['activity']
    activity_log.notes = request.POST['notes']
    activity_log.save()

def delete_activity_log(request, id):
    activity_log = ActivityLog.objects.get(pk=id)
    activity_log.delete()
