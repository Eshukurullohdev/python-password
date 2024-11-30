from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db import IntegrityError


def home_page(request):
    tovar = Tovar.objects.all()
    cartCount = Cart.objects.count()
    return render(request, "home.html", {
        "tovar": tovar,
        "cartlarSoni": cartCount
        }
    )


def footer_page(request):
    return render(redirect, "footer.html")


def sidebar_page(request):
    return render(request, "sidebar.html")


def discount_page(request):
    tovar = Tovar.objects.all().filter(skitka=True)
    return render(request, "discount.html", {"tovar": tovar})


def gadjet_page(request):
    tovar = Gadjet.objects.all()
    return render(request, "gadjet.html", {"tovar": tovar})


def texnika_page(request):
    tovar = Texnika.objects.all()
    return render(request, "texnika.html", {"tovar": tovar})


def kitob_page(request):
    tovar = Kitob.objects.all()
    return render(request, "book.html", {"tovar": tovar})


def televizor_page(request):
    tovar = Tv.objects.all()
    return render(request, "tv.html", {"tovar": tovar})


def expensive_page(request):
    tovar = Expesiv.objects.all()
    return render(request, "expensiv.html", {"tovar": tovar})


def notebook_page(request):

    if request.method == "POST":
        message = request.POST.get("text")
        Smm.objects.create(
            message = message,
        )
        return redirect("/")
    tovar = Notebook.objects.all()
    return render(request, "notebook.html", {"tovar": tovar})


def buy_page(request):
    tovar = Tovar.objects.all()
    return render(request, "buy.html", {"tovar": tovar})


def tovar_page(request, tovarni_idsi):


    tovar =Tovar.objects.filter(unique_id=tovarni_idsi).exists()
    gadjet =Gadjet.objects.filter(unique_id=tovarni_idsi).exists()
    notebook=Notebook.objects.filter(unique_id=tovarni_idsi).exists()
    kitob=Kitob.objects.filter(unique_id=tovarni_idsi).exists()
    expesive=Expesiv.objects.filter(unique_id=tovarni_idsi).exists()
    tv=Tv.objects.filter(unique_id=tovarni_idsi).exists()
    texnika=Texnika.objects.filter(unique_id=tovarni_idsi).exists()


    if tovar:
        tovar_m =Tovar.objects.get(unique_id=tovarni_idsi)
        if request.method == "POST":
            message =request.POST.get("text")
            Smm.objects.create(message=message, tovar=tovar_m)
            return redirect("/tovar/" + tovarni_idsi + "/")
    elif gadjet:
        tovar_m =Gadjet.objects.get(unique_id=tovarni_idsi)
        if request.method == "POST":
            message =request.POST.get("text")
            Smm.objects.create(message=message, gadjet=tovar_m)
            return redirect("/tovar/" + tovarni_idsi + "/")
    elif notebook:
        tovar_m =Notebook.objects.get(unique_id=tovarni_idsi)
        if request.method == "POST":
            message =request.POST.get("text")
            Smm.objects.create(message=message, notebook=tovar_m)
            return redirect("/tovar/" + tovarni_idsi + "/")
    elif kitob:
        tovar_m=Kitob.objects.get(unique_id=tovarni_idsi)
        if request.method == "POST":
            message =request.POST.get("text")
            Smm.objects.create(message=message, kitob=tovar_m)
            return redirect("/tovar/" + tovarni_idsi + "/")
    elif expesive:
        tovar_m=Expesiv.objects.get(unique_id=tovarni_idsi)
        if request.method == "POST":
            message =request.POST.get("text")
            Smm.objects.create(message=message, expesive=tovar_m)
            return redirect("/tovar/" + tovarni_idsi + "/")
    elif tv:
        tovar_m=Tv.objects.get(unique_id=tovarni_idsi)
        if request.method == "POST":
            message =request.POST.get("text")
            Smm.objects.create(message=message, tv=tovar_m)
            return redirect("/tovar/" + tovarni_idsi + "/")

    elif texnika:
        tovar_m=Texnika.objects.get(unique_id=tovarni_idsi)
        if request.method == "POST":
            message =request.POST.get("text")
            Smm.objects.create(message=message, texnika=tovar_m)
            return redirect("/tovar/" + tovarni_idsi + "/")

    else:
        tovar_m = False
        
    context= {
        "tovar": tovar_m,
    }
    return render(request, "tovar.html", context)


def search_page(request):
    tovar = Tovar.objects.all()
    gadjets = Gadjet.objects.all()
    tvs = Tv.objects.all()
    texnniks = Texnika.objects.all()
    kitobs = Kitob.objects.all()
    news = Expesiv.objects.all()
    noutbook = Notebook.objects.all()
    natijalar = []

    if request.method == "GET":
        key = request.GET.get("key")
        if key:
            tovar = Tovar.objects.all().filter(name__icontains=key)
            if tovar:
                natijalar.append(tovar)
            gadjets = Gadjet.objects.all().filter(name__icontains=key)
            if gadjets:
                natijalar.append(gadjets)
            tvs = Tv.objects.all().filter(name__icontains=key)
            if tvs:
                natijalar.append(tvs)
            texnniks = Texnika.objects.all().filter(name__icontains=key)
            if texnniks:
                natijalar.append(texnniks)
            kitobs = Kitob.objects.all().filter(name__icontains=key)
            if kitobs:
                natijalar.append(kitobs)
            news = Expesiv.objects.all().filter(name__icontains=key)
            if news:
                natijalar.append(news)
            noutbook = Notebook.objects.all().filter(name__icontains=key)
            if noutbook:
                natijalar.append(noutbook)

    context = {
        "tovar": tovar,
        "key": key,
        "gadjet": gadjets,
        "tv": tvs,
        "texnika": texnniks,
        "kitob": kitobs,
        "yangi": news,
        "noutbook": noutbook,
        "natijalar": natijalar,
    }
    return render(request, "search.html", context)


def shopingCart_page(request):
    carst = Cart.objects.all()
    context = {"carts": carst}
    return render(request, "shoppingCart.html", context)


#  login register logaut


def register_page(request):
    if not request.user.is_authenticated:
        try:
            if request.method == "POST":
                username = request.POST.get("username")
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name")
                email = request.POST.get("email")
                password = request.POST.get("password")
                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=make_password(password),
                )
                login(request, user)
                return redirect("/")
        except IntegrityError as e:
            messages.error(request, f"siz register {e}, bor")
        return render(request, "register.html")
    else:
        return redirect("/")


def login_page(request):
    if not request.user.is_authenticated:
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=make_password(password))
            if user:
                login(request, user)
                return redirect("/")
            else:
                messages.warning(request, "bunday user mavjud emas")
        except:
            print("xato")
        return render(request, "login.html")
    else:
        return redirect("/")


def logaut_page(request):
    logout(request)
    return redirect("/")


def add_to_cart_page(request, tovarni_idsi):

    try:
        gadjet = Gadjet.objects.get(unique_id=tovarni_idsi)
        try:
            Cart.objects.get(gadjet=gadjet)
            messages.warning(request, "Savatchangizda allaqachon bunday tovar mavjud")
            return redirect("/")
        except:
            Cart.objects.create(gadjet=gadjet)
    except Gadjet.DoesNotExist:
        print("Tovar mavjud emas")

    try:
        tovar = Tovar.objects.get(unique_id=tovarni_idsi)
        try:
            Cart.objects.get(tovar=tovar)
            return redirect("/")
        except:
            Cart.objects.create(tovar=tovar)
    except Tovar.DoesNotExist:
        print("Tovar mavjud emas")

    try:
        texnika = Texnika.objects.get(unique_id=tovarni_idsi)
        try:
            Cart.objects.get(texnika=texnika)
            return redirect("/")
        except:
            Cart.objects.create(texnika=texnika)
    except Texnika.DoesNotExist:
        print("Tovar mavjud emas")

    return redirect("/")


def savatchadan_olib_tashlamoq(request, cart_idsi):
    try:
        cart = Cart.objects.get(id=cart_idsi)
        cart.delete()
        return redirect("/cart/")
    except:
        pass


def like_pageni_korsatish(request):
    likes = ThumbsUp.objects.all()
    context = {"likes": likes}
    return render(request, "like.html", context)


def add_to_like(request, tovarni_idsi):
    try:
        gadjet = Gadjet.objects.get(unique_id=tovarni_idsi)
        try:
            ThumbsUp.objects.get(gadjet=gadjet)
        except:
            ThumbsUp.objects.create(gadjet=gadjet)
    except Gadjet.DoesNotExist:
        pass


    try:
        expesive = Expesiv.objects.get(unique_id=tovarni_idsi)
        try:
            ThumbsUp.objects.get(expesive=expesive)
        except:
            ThumbsUp.objects.create(expesive=expesive)
    except Expesiv.DoesNotExist:
        pass

    return redirect("/")
