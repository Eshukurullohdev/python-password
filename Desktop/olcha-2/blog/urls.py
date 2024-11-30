from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home"),
    path("register/", register_page, name='register'),
    path("login/", login_page, name='login'),
    path("logaut/", logaut_page, name='logaut'),
    path("discount/", discount_page, name='discount'),
    path("sidebar/",sidebar_page, name='sidebar' ),
    path("gadjet/", gadjet_page, name='gadjet'),
    path("texnika/", texnika_page, name='texnika'),
    path("kitob/", kitob_page, name='kitob'),
    path("tv/", televizor_page, name='tv'),
    path("expensiv/", expensive_page, name='expensiv'),
    path("notebook/", notebook_page, name='notebook'),
    path("product/", search_page, name='search'), 
    path("cart/", shopingCart_page, name='shoppingCart'),
    path("buy/",buy_page, name='buy'),
    path("tovar/<str:tovarni_idsi>/", tovar_page, name='tovar'),
    path('add_to_cart/<str:tovarni_idsi>/', add_to_cart_page, name='add_to_cart'),
    path("olib-tashlash/<int:cart_idsi>/", savatchadan_olib_tashlamoq, name='cart_remove'),
    path("like/<str:tovarni_idsi>/", add_to_like, name='add_to_like'),
    path("likes/", like_pageni_korsatish, name='like_page')
]

# olib-tashlash/3