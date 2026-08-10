from django.urls import path
from . import views
urlpatterns=[
    path('m1/',views.message1),
    path('m2/',views.message2),
    path('m3/',views.message3),
    path('m4/',views.message4)
]