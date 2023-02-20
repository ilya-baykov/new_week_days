from django.contrib import admin
from django.urls import path, include
from week_days_app import views as days

urlpatterns = [
    path('monday', days.monday),
    path('tuesday', days.tuesday),
    path('wednesday', days.wednesday),
    path('thursday', days.thursday),
    path('friday', days.friday),
    path('saturday', days.saturday),
    path('sunday', days.sunday)

]
