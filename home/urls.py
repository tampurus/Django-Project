from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [

    #old
    # path('',views.index, name='home'),
    # path('home',views.index, name='home'), # url agey home likho ya nhi ana home pr hi hai
    # path('about',views.about, name='about'), 
    # path('contact',views.contact, name='contact'),

    # changed
    path('',views.index),
    path('home',views.index), # url agey home likho ya nhi ana home pr hi hai start me
    path('about',views.about), 
    path('contact',views.contact),
]