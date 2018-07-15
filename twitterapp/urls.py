from django.contrib import admin
from django.urls import path, include
from twitterapp.views import *

urlpatterns = [
    path('', form_twit),
    path('user/<int:pk>', user),
    path('user/edit/<int:pk>', edit_twit, name="edit_twit"),
    path('retwit/<int:pk>', retwit, name="re_twit"),
    path('user/profile/', edit_profile),
    path('message/<int:pk>', twit_single, name="twit_single")
]