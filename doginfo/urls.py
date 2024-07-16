from django.urls import path
from . import views


urlpatterns = [
    path("info/<id>/", views.view_dog_by_id, name="view_dog_by_id"),
    path("info/<dog_name>/", views.view_dog_by_name, name="view_dog_by_name"),
    path("info/", views.view_dogs, name="view_dogs"),
    path("info/create/", views.create_dog, name="create_dog"),
    path("info/update/<id>/", views.update_dog, name="update_dog"),
    path("info/delete/<id>/", views.delete_dog, name="delete_dog"),
    path("feeding_schedule/", views.view_feeding_schedule, name="view_feeding_schedule"),
    path("feeding_schedule/<dog_id>/", views.view_feeding_schedule_for_dog, name="view_feeding_schedule_for_dog"),
    path("feeding_schedule/create/", views.create_feeding_schedule, name="create_feeding_schedule"),
    path("feeding_schedule/update/<id>/", views.update_feeding_schedule, name="update_feeding_schedule"),
    path("feeding_schedule/delete/<id>/", views.delete_feeding_schedule, name="delete_feeding_schedule"),
    path("activity_log/", views.view_activity_log, name="view_activity_log"),
    path("activity_log/create/", views.create_activity_log, name="create_activity_log"),
    path("activity_log/update/<id>/", views.update_activity_log, name="update_activity_log"),
    path("activity_log/delete/<id>/", views.delete_activity_log, name="delete_activity_log"),

]