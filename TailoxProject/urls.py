from django.contrib import admin
from django.urls import path,include

urlpatterns =[
        path('admin/', admin.site.urls ),  # new
        path('', include('TailorxApp.urls')),  # new
]