from django.contrib import admin
from .models import *

MODELS = [
    Tovar, Cart, Gadjet,
    Texnika, Kitob, Tv,
    Expesiv, Notebook, ThumbsUp,
    Smm
]

[admin.site.register(model) for model in MODELS]

# Register your models here.
