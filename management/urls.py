from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index,name="index"),
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('booking',views.booking,name="booking"),
    path('doctors',views.doctors,name="doctors"),
    path('contact',views.contact,name="contact"),
    path('department',views.department,name="department"),
    path('registration',views.registration,name="registration"),
    path('login',views.loginn,name="login"),
    path('logout', views.user_logout, name='logout'),
]