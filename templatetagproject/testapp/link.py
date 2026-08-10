from django.urls import path
from . import views
urlpatterns=[
    path('see/', views.tags),
    path('msg/',views.msg)
]