from django.urls import path
from movieapp import views

urlpatterns = [
    path('',views.registeration,name='register'),
    path('index/',views.index,name='index'),
    path('login',views.login_use,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('create_admin/',views.create_admin, name='create_admin'),
    # path('submit/',views.submit, name='submit'),
    ]