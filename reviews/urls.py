from django.urls import path , include
from . import views

urlpatterns = [
    path('makereview/', views.makereview, name='makereview'),
    path('all_reviews', views.all_reviews, name = 'all_reviews'),
    path('<int:review_id>/', views.review_detailed, name='review_detailed'),
]
