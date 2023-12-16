from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Customers', CustomersViewSet, basename='Customers')
router.register('Products', ProductsViewSet, basename='Products')
router.register('Orders', OrdersViewSet, basename='Orders')
router.register('Reviews', ReviewsViewSet, basename='Reviews')

urlpatterns = [
  path('viewset/', include(router.urls)),

]
