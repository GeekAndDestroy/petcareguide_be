from rest_framework import serializers
from .models import Dog, FeedingSchedule, ActivityLog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'breed', 'est_dob', 'weight', 'sex', 'medical_conditions']
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=100)
    # breed = serializers.CharField(max_length=100)
    # est_dob = serializers.DateField()
    # weight = serializers.PositiveSmallIntegerField()
    # sex = serializers.CharField(max_length=1)
    # medical_conditions = serializers.TextField()

class feedingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedingSchedule
        fields = ['id', 'dog', 'food', 'amount', 'frequency']
    # id = serializers.IntegerField(read_only=True)
    # dog = DogSerializer()
    # food = serializers.CharField(max_length=100)
    # amount = serializers.PositiveSmallIntegerField()
    # frequency = serializers.CharField(max_length=100)

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = ['id', 'dog', 'activity', 'notes']
    # id = serializers.IntegerField(read_only=True)
    # dog = serializers.IntegerField(write_only=True)
    # dog = DogSerializer()
    # activity = serializers.CharField(max_length=100)
    # notes = serializers.TextField()