# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from .views import ProductViewSet

# product_list = ProductViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)