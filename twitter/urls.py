
from django.contrib import admin
from django.urls import path, include
from twitterapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('twitterapp.urls')),
    path('accounts/', include('allauth.urls')),
]