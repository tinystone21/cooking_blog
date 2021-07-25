from django.urls import path

from .views import (
    MainPageView, CategoryDetailView,
    RecipeDetailView, add_recipe, RecipeUpdateView,
    RecipeDeleteView, UserRegistrationView, AuthorizationView
)


urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path(
        'category/<str:slug>/', CategoryDetailView.as_view(),
        name='category'
    ),
    path('recipe-detail/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
    path('add-recipe/', add_recipe, name='add-recipe'),
    path(
        'update-recipe/<int:pk>/',
        RecipeUpdateView.as_view(), name='update-recipe'
    ),
    path(
        'delete-recipe/<int:pk>/', RecipeDeleteView.as_view(),
        name='delete-recipe'
    ),
    path(
        'registration-detail/', UserRegistrationView.as_view(),
        name='registration'
    ),
    path('login/', AuthorizationView.as_view(), name='login')
]
