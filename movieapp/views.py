from django.shortcuts import render,redirect
from movieapp.forms import UserForm,UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from django.http import JsonResponse
from .models import Review
from django.contrib.auth.models import User



# Create your views here.

def registeration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form1 = UserProfile(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')
    else:
        form = UserForm()
        form1 = UserProfile()
    context = {'form':form,'form1':form1
               }
    return render (request,'register.html',context)



def login_use(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse('user not active..')
        else:
            return HttpResponse('please check credentials..')

    return render(request,'login.html',{})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login") 
def index(request):
    movie_title = request.GET.get("movie")


    if request.method == "POST":

        
        rating = request.POST.get("rating")
        review_text = request.POST.get("review")


        if rating and review_text:
            Review.objects.create(
                user=request.user,
                movie_title=movie_title,
                rating=rating,
                review=review_text
            )

    reviews = Review.objects.filter(
        movie_title=movie_title
    ).order_by("-id")[:5]

    return render(request, 'index.html', {
        "reviews": reviews,
        "movie_title": movie_title
    })


def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            password="admin123",
            email="admin@test.com"
        )
        return HttpResponse("Admin created")
    return HttpResponse("Admin already exists")