from django.urls import path


from .views import CartView, ShopView, ProductSingleView


urlpatterns = [
    path('', CartView.as_view()),
    path('', ShopView.as_view()),
    path('', ProductSingleView.as_view())
]