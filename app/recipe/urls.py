from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

# este lo que hace es generar rutas a través de un viewset
router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
