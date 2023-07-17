from django.urls import path
from .user_views import *



urlpatterns=[

    path('',HomeView.as_view(),name='home'),
    path('/register',RegisterView.as_view(), name='register'),
    path('/connexion',ConnexionView.as_view(), name='connexion'),
    path('/contact',ContactView.as_view(), name='contact'),
    path('/about',AboutView.as_view(), name='about'),
    path('/shop',ShopView.as_view(), name='shop'),
    path('/cart',CartView.as_view(), name='cart'),
    path('/checkout',CheckoutView.as_view(), name='checkout'),
    path('/thankyou',ThankyouView.as_view(), name='thankyou'),
    path('/shop-single',ShopsingleView.as_view(), name='shop-single')

]
