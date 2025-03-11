from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def nav(request):
    return render(request, 'nav.html')

def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # ✅ Sahifani qayta yuklash

    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-created_at')  # ✅ Eng yangi postlarni birinchi chiqarish

    return render(request, 'home.html', {'form': form, 'posts': posts})


