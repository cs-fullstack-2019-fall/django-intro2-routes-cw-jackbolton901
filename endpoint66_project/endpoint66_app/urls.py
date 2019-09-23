from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("gogetthegood/", views.goods),
    path("happyhappyjoyjoy/", views.happy),
]