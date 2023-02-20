from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def monday(request):
    return HttpResponse(f"Понедельник - день тяжелый :c")


def tuesday(request):
    return HttpResponse(f"Вторник - хе хе мне уже лучше !")


def wednesday(request):
    return HttpResponse(f"Ура! Уже середина недели !!!")


def thursday(request):
    return HttpResponse(f"Четверг! Странно...Но мне нравится этот день!!! ")


def friday(request):
    return HttpResponse(f"УРААААА! ПЯТНИЦА !!! ТУЦ ТУЦ ТУЦ :3")


def saturday(request):
    return HttpResponse(f"Ну вот , уже суббота , можно отоспаться хихихих")


def sunday(request):
    return HttpResponse(f"Воскресенье - пора готовиться к следующей недели ;3333")
