from django.urls import include, path
from rest_framework_nested import routers
from . import views


# Parent router
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)

# Nested router
product_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')  # Have product_id params in url
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')

# URLConf
urlpatterns = router.urls + product_router.urls
