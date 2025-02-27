from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register('recipes', RecipeViewSet)

recipe_urls = router.urls