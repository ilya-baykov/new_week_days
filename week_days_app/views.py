from typing import List, Any

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
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


def validation_str(url: str) -> bool:
    return isinstance(url, str) and url in week_days_info_data


def validation_int(url: str) -> bool:
    return len(re.findall(r'\b[1-7]', url)) > 0


def give_info_about_days(requst, current_day: str | int):
    if validation_str(current_day):
        return HttpResponse(f"{week_days_info_data[current_day]}")
    elif validation_int(current_day):
        return HttpResponse(f"{list(week_days_info_data)[int(current_day) - 1]}")
    else:
        return HttpResponseNotFound(f"{current_day} - такая страница не найдена ;с")


def current_day_int_info(request, current_day_digit):
    return HttpResponse(f"Вы ввели число, а я это отловил хихихихих")
