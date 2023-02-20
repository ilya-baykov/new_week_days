from django.contrib import admin
from django.urls import path, include
from week_days_app import views as days

urlpatterns = [
    path("<int:current_day_digit>", days.current_day_int_info),
    path("<str:current_day_stry>", days.give_info_about_days)

]
