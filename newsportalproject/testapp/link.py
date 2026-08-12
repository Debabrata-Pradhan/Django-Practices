from django.urls import path

from . import views

urlpatterns=[
    path('movies/',views.movies),
    path('sports/',views.sports),
    path('politics/',views.politics)
]