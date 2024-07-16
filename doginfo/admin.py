from django.contrib import admin
from .models import Dog, FeedingSchedule, ActivityLog

admin.site.register(Dog)
admin.site.register(FeedingSchedule)
admin.site.register(ActivityLog)
