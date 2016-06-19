from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'images', views.ImageViewSet)
