from django.urls import path
from kitchen.views import (
    index,

    CookListView,
    CookDetailView,
    CookCreateView,
    CookExperienceUpdateView,
    CookDeleteView,

    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,

    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,

    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
)


urlpatterns = [
    path("kitchen/", index, name="index"),


    path(
        "dish-type/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dish-type/create",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish-type/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish-type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),


    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list",
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail",
    ),
    path(
        "cooks/create/",
        CookCreateView.as_view(),
        name="cook-create",
    ),
    path(
        "cooks/<int:pk>/update/",
        CookExperienceUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),


    path(
        "ingredients/",
        IngredientListView.as_view(),
        name="ingredient-list",
    ),
    path(
        "ingredients/create",
        IngredientCreateView.as_view(),
        name="ingredient-create",
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),


    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail",
    ),
    path(
        "dishes/create",
        DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update",
    ),

]

app_name = "kitchen"
