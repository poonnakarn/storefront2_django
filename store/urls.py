from rest_framework_nested import routers
from . import views


# Parent router
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet, basename='carts')
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

# Nested router
products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')  # Have product_id params in url
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')
# Nested router
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls
