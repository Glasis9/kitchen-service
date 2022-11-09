from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from kitchen.models import Dish, Cook, DishType


@login_required
def index(request):
    num_dish = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_dish_type = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dish": num_dish,
        "num_cooks": num_cooks,
        "num_dish_type": num_dish_type,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)
