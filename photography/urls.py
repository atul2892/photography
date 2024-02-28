from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('service/',views.service),
    path('project/',views.project),
    path('project-single/',views.projectSingle),
    path('rent/',views.rent),
    path('team/',views.team),
    path('gallery/',views.gallery),
    path('contact/',views.contact),
]
