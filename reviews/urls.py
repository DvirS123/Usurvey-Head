from django.urls import path , include
from . import views

urlpatterns = [
    path('makereview/', views.makereview, name='makereview'),
]
