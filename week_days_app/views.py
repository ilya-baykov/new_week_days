from typing import List, Any

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import re

# Create your views here.

week_days_info_data = {
    "monday": "Понедельник - день тяжелый :c",
    "tuesday": "Вторник - хе хе мне уже лучше !",
    "wednesday": "Ура! Уже середина недели !!",
    "thursday": "Четверг! Странно...Но мне нравится этот день!!!",
    "friday": "УРААААА! ПЯТНИЦА !!! ТУЦ ТУЦ ТУЦ :3",
    "saturday": "Ну вот , уже суббота , можно отоспаться хихихих",
    "sunday": "Воскресенье - пора готовиться к следующей недели ;3333",
    "meme": "Не умею дебажить - страдаю хуйней ;с",
}


def give_info_about_days(request, current_day_stry: str):
    info = week_days_info_data.get(current_day_stry, 0)
    if info:
        return HttpResponse(week_days_info_data[current_day_stry])
    else:
        return HttpResponseNotFound(f"Мы не знамем такую страницу ;с  {current_day_stry}")


def current_day_int_info(request, current_day_digit):
    if 8 > current_day_digit > 0:
        return HttpResponseRedirect(f'/week_days/{list(week_days_info_data)[current_day_digit - 1]}')
    else:
        return HttpResponseNotFound(f"Мы не день под таким числом ( доступен ввод от 1 до 7 ) , вы ввели - {current_day_digit}")

