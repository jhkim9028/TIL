from itertools import product
from django.shortcuts import render
import random

# Create your views here.


def number(request, _number):
    data = _number

    if data % 2 == 0:
        type = "짝수"
    else:
        type = "홀수"

    context = {
        "number": data,
        "type": type,
    }
    return render(request, "number.html", context)


def calculate(request, _num1, _num2):
    num1 = _num1
    num2 = _num2
    sum = _num1 + _num2
    minus = _num1 - _num2
    mul = _num1 * _num2
    div = _num1 // _num2
    context = {
        "number1": num1,
        "number2": num2,
        "sum": sum,
        "minus": minus,
        "mul": mul,
        "div": div,
    }
    return render(request, "calculate.html", context)


def input_(request):
    return render(request, "input_.html")


def pastlife(request):
    animal = ["말", "돼지", "소", "닭", "개", "원숭이", "토끼", "호랑이", "용", "쥐", "뱀", "양"]
    name = request.GET.get("name")
    past = random.choice(animal)
    context = {
        "player": name,
        "past_": past,
    }
    return render(request, "pastlife.html", context)


def lorem(request):
    return render(request, "lorem.html")


def lipsum(request):
    food = ["바나나", "짜장면", "사과", "포도", "딸기"]
    paragraph_ = request.GET.get("paragraph")
    word_ = request.GET.get("word")

    food_ = []

    for _ in range(int(word_)):
        food_.append(random.choice(food))

    context = {
        "food_": food_,
    }
    return render(request, "lipsum.html", context)
