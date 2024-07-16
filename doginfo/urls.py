from django.urls import path
from . import views


urlpatterns = [
    path("<int:id>/", views.dog_detail, name="view_dog_by_id"),
    path("", views.dogs_list),
    path("feeding_schedule/", views.feeding_schedule_list),
    path("feeding_schedule/<int:dog_id>/", views.feeding_schedule_detail),
    path("activity_log/", views.activity_log_list),
    path("activity_log/<int:id>/", views.activity_log_detail)]