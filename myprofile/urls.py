# backend/urls.py
from django.contrib import admin
from django.urls import path
from myprofile.views import create_profile, list_profiles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/profile/', create_profile, name='create-profile'),
    path('api/profile/list/', list_profiles, name='list-profiles'),
]
