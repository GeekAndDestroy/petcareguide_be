from django.shortcuts import get_object_or_404
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# from django.http import HttpResponse
from .models import Dog, FeedingSchedule, ActivityLog
from .serializers import DogSerializer, feedingScheduleSerializer, ActivityLogSerializer
# terst
@api_view(['GET', 'POST'])
def dogs_list(request):
    if request.method == 'GET':
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def dog_detail(request, id):
    dog = get_object_or_404(Dog, pk=id)
    if request.method == 'GET':
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DogSerializer(dog, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def create_dog(request):
#     dog = Dog()
#     dog.name = request.POST.get('name')
#     dog.breed = request.POST.get('breed')
#     dog.est_dob = request.POST.get('est_dob')
#     dog.weight = request.POST.get('weight')
#     dog.sex = request.POST.get('sex')
#     dog.medical_conditions = request.POST.get('medical_conditions')
#     dog.save()
#     jsondata = serializers.serialize('json', dog)
#     return Response(jsondata, content_type='application/json')
    # return Response(dog)

# @api_view(['PUT'])
# def update_dog(request, id):
#     dog = Dog.objects.get(pk=id)
#     dog.name = request.POST.get('name')
#     dog.breed = request.POST.get('breed')
#     dog.est_dob = request.POST.get('est_dob')
#     dog.weight = request.POST.get('weight')
#     dog.sex = request.POST.get('sex')
#     dog.medical_conditions = request.POST.get('medical_conditions')
#     dog.save()

# @api_view(['DELETE'])
# def delete_dog(request, id):
#     dog = Dog.objects.get(pk=id)
#     dog.delete()

@api_view(['GET', 'POST'])
def feeding_schedule_list(request):
    if request.method == 'GET':
        feeding_schedule = FeedingSchedule.objects.select_related('dog').all()
        serializer = feedingScheduleSerializer(feeding_schedule, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = feedingScheduleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def feeding_schedule_detail(request, dog_id):
    feeding_schedule = get_object_or_404(FeedingSchedule, dog=dog_id)
    if request.method == 'GET':
        serializer = feedingScheduleSerializer(feeding_schedule)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = feedingScheduleSerializer(feeding_schedule, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        feeding_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def create_feeding_schedule(request):
#     feeding_schedule = FeedingSchedule()
#     feeding_schedule.dog = Dog.objects.get(pk=request.POST.get('dog_id'))
#     feeding_schedule.food = request.POST.get('food')
#     feeding_schedule.amount = request.POST.get('amount')
#     feeding_schedule.frequency = request.POST.get('frequency')
#     feeding_schedule.save()

# @api_view(['PUT'])
# def update_feeding_schedule(request, id):
#     feeding_schedule = FeedingSchedule.objects.get(pk=id)
#     feeding_schedule.dog = Dog.objects.get(pk=request.POST['dog_id'])
#     feeding_schedule.food = request.POST['food']
#     feeding_schedule.amount = request.POST['amount']
#     feeding_schedule.frequency = request.POST['frequency']
#     feeding_schedule.save()

# @api_view(['DELETE'])
# def delete_feeding_schedule(request, id):
#     feeding_schedule = FeedingSchedule.objects.get(pk=id)
#     feeding_schedule.delete()

@api_view(['GET', 'POST'])
def activity_log_list(request):
    if request.method == 'GET':
        activity_log = ActivityLog.objects.select_related('dog').all()
        serializer = ActivityLogSerializer(activity_log, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ActivityLogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def activity_log_detail(request, id):
    activity_log = get_object_or_404(ActivityLog, id)

    if request.method == 'PUT':
        serializer = ActivityLogSerializer(activity_log, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        activity_log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def activity_log_detail_by_dog(request, dog_id):
    # activity_logs = get_object_or_404(ActivityLog, dog=dog_id)
    activity_logs = ActivityLog.objects.filter(dog=dog_id)
    serializer = ActivityLogSerializer(activity_logs, many=True)
    return Response(serializer.data)
    

# @api_view(['POST'])
# def create_activity_log(request):
#     activity_log = ActivityLog()
#     activity_log.dog = Dog.objects.get(pk=request.POST.get('dog_id'))
#     activity_log.activity = request.POST.get('activity')
#     activity_log.notes = request.POST.get('notes')
#     activity_log.save()

# @api_view(['PUT'])
# def update_activity_log(request, id):
#     activity_log = ActivityLog.objects.get(pk=id)
#     activity_log.dog = Dog.objects.get(pk=request.POST.get('dog_id'))
#     activity_log.activity = request.POST.get('activity')
#     activity_log.notes = request.POST.get('notes')
#     activity_log.save()

# @api_view(['DELETE'])
# def delete_activity_log(request, id):
#     activity_log = ActivityLog.objects.get(pk=id)
#     activity_log.delete()
