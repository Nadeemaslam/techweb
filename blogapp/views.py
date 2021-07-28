from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    blogs = Post.objects.filter(status=1).order_by('-created_on')[:10]
    context = {'Post': blogs}
    return render(request, 'blogapp/index.html', context)

def blogs(request):
    return render(request,  template_name='blogapp/blog.html')


def detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        context = {'post': post}
        return render(request, 'blogapp/detail.html', context)
    except ObjectDoesNotExist:
        return render(request,  template_name='blogapp/detail.html')


def about(request):
    return render(request,  template_name='blogapp/about.html')

def loginPage(request):

    # form = CreateUserForm()
    # context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or Password Incorrect')
            return render(request, 'accounts/login.html',)
    else:
        return render(request, 'accounts/login.html',)


def logoutUser(request):

    logout(request)
    return redirect('login')



def contact(request):
    return render(request, template_name='blogapp/contact.html')


def products(request):
    return render(request, template_name='mainapp/products.html')